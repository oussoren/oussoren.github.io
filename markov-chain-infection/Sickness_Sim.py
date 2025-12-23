import math
import numpy as np
import scipy.stats as stats
import numpy.linalg
import matplotlib.pyplot as plt
import os
import seaborn as sns

# --- I. Model Parameters ---
DECAY_RATE = 0.3
MAX_RATE = 0.1  # Use 0.035 for better results in 60 mins
P_BASE = 1.0 / 9.0


# --- II. Core Helper Functions ---

def eval_position(tile_index, width):
    """Maps a 1D tile index to 2D coordinates."""
    y = tile_index // width + 1
    x = tile_index % width + 1
    return x, y


def get_tile_index(x, y, width):
    """Maps 2D coordinates back to 1D tile index."""
    # x, y are 1-based. Index is 0-based.
    return (y - 1) * width + (x - 1)


def get_valid_moves_and_probs(start_index, width):
    """
    Returns a list of tuples: [(next_tile_index, probability), ...]
    This replaces looping through the whole grid.
    """
    moves = []
    x, y = eval_position(start_index, width)

    # Identify all neighbors (including self)
    neighbors = []
    blocked_count = 0

    # Check all 8 directions + stay (dx, dy from -1 to 1)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # We handle 'Stay' separately at the end

            nx, ny = x + dx, y + dy

            # Check if wall
            if nx < 1 or nx > width or ny < 1 or ny > width:
                blocked_count += 1
            else:
                # Valid neighbor
                n_idx = get_tile_index(nx, ny, width)
                neighbors.append(n_idx)

    # 1. Add probability for moving to valid neighbors
    for n_idx in neighbors:
        moves.append((n_idx, P_BASE))

    # 2. Add probability for Staying Put (Base + Absorbed Wall Bumps)
    stay_prob = P_BASE + (blocked_count * P_BASE)
    moves.append((start_index, stay_prob))

    return moves


# --- III. Matrix Constructors (Optimized) ---

def construct_mvmt_mtx(room_width):
    """
    Optimized construction.
    Instead of 43 million loops, we only process valid moves (~500k ops).
    """
    n = room_width ** 2
    num_states = n * n
    m = np.zeros((num_states, num_states))

    # 1. Loop through all Starting States (i)
    for t_s in range(n):
        # Pre-calculate valid moves for Sick person from this tile
        moves_s = get_valid_moves_and_probs(t_s, room_width)

        for t_h in range(n):
            # Pre-calculate valid moves for Healthy person from this tile
            moves_h = get_valid_moves_and_probs(t_h, room_width)

            # Current State Index i
            i = (t_s * n) + t_h

            # 2. Iterate ONLY over valid next steps (j)
            # This replaces the inner 2 loops (81*81 iterations) with just ~9*9 iterations
            for (next_s, prob_s) in moves_s:
                for (next_h, prob_h) in moves_h:
                    # Target State Index j
                    j = (next_s * n) + next_h

                    # Set Probability
                    m[i, j] = prob_s * prob_h

    return m


def calc_distance(sick_index, healthy_index, room_width):
    sick_pos = eval_position(sick_index, room_width)
    healthy_pos = eval_position(healthy_index, room_width)
    return math.sqrt(((sick_pos[0] - healthy_pos[0]) ** 2) + ((sick_pos[1] - healthy_pos[1]) ** 2))


def prob_healthy(distance):
    lam = MAX_RATE * (math.e ** (-1 * DECAY_RATE * distance))
    # Poisson PMF at 0 is just e^-lambda
    return math.exp(-lam)


def construct_infect_mtx(width):
    n = width ** 2
    num_states = n * n
    s = np.zeros((num_states, num_states))
    for i in range(num_states):
        t_s = i // n
        t_h = i % n
        distance = calc_distance(t_s, t_h, width)
        p_survival = prob_healthy(distance)
        s[i, i] = p_survival
    return s


def calculate_transition_matrix(m, s, width):
    n = width * width
    num_states = n * n

    # Q = M x S
    Q = m @ s

    # Calculate Leak Vector R
    R = 1.0 - np.sum(Q, axis=1)

    n_total = num_states + 1
    P = np.zeros((n_total, n_total))

    # Fill P
    P[:num_states, :num_states] = Q
    P[:num_states, num_states] = R  # R is flat array, fits into column
    P[num_states, num_states] = 1.0

    return P


def simulate_room(width, sick_start_tile_index, healthy_start_tile_index, time_steps=60):
    print(f"Constructing matrices for {width}x{width} room...")
    n = width * width
    num_states = n * n
    n_total = num_states + 1

    m = construct_mvmt_mtx(width)
    s = construct_infect_mtx(width)
    P = calculate_transition_matrix(m, s, width)

    print("Matrices built. Simulating steps...")

    starting_state_index = sick_start_tile_index * n + healthy_start_tile_index
    v0 = np.zeros(n_total)
    v0[starting_state_index] = 1.0

    P_k = np.linalg.matrix_power(P, time_steps)
    v_k = v0 @ P_k

    return v_k[-1]


def generate_visual(width, s_idx, h_idx, time_steps=120):
    print("Generating visualization data...")
    n = width * width
    num_states = n * n

    # 1. Build the matrix once
    m = construct_mvmt_mtx(width)
    s = construct_infect_mtx(width)
    P = calculate_transition_matrix(m, s, width)

    # 2. Track probability over time
    starting_state_index = s_idx * n + h_idx
    v = np.zeros(num_states + 1)
    v[starting_state_index] = 1.0

    time_axis = []
    prob_axis = []

    for t in range(time_steps + 1):
        time_axis.append(t)
        prob_axis.append(v[-1])  # The last entry is our 'Sick' state
        v = v @ P  # Step forward by 1 minute

    # 3. Create a professional plot
    plt.style.use('seaborn-v0_8-muted')  # Clean, modern look
    plt.figure(figsize=(10, 5))
    plt.plot(time_axis, prob_axis, color='#e74c3c', linewidth=2.5, label='P(Infected)')

    plt.title(f'Accumulated Infection Risk: {width}x{width} Room', fontsize=14, pad=15)
    plt.xlabel('Time Elapsed (Minutes)', fontsize=12)
    plt.ylabel('Probability of Infection', fontsize=12)
    plt.ylim(0, 1.05)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # SAVE THIS to your Hugo images folder
    os.makedirs('static/images', exist_ok=True)

    plt.savefig('static/images/infection_plot.png', dpi=300)
    # Note: Make sure the directory 'static/images/' exists first
    print("Saved plot to static/images/infection_plot.png")
    plt.show()


def generate_heatmap(width, s_idx, time_steps=60):
    print(f"Generating {width}x{width} Heat Map (this may take a moment)...")

    # 1. Build the matrix once (the expensive part)
    m = construct_mvmt_mtx(width)
    s = construct_infect_mtx(width)
    P = calculate_transition_matrix(m, s, width)
    P_k = np.linalg.matrix_power(P, time_steps)

    n = width * width
    heatmap_data = np.zeros((width, width))

    # 2. Test every possible starting position for the healthy person
    for h_idx in range(n):
        v0 = np.zeros(n ** 2 + 1)
        start_state = (s_idx * n) + h_idx
        v0[start_state] = 1.0

        # Multiply by the powered matrix
        v_k = v0 @ P_k
        prob = v_k[-1]

        # Map 1D index back to 2D for the plot
        x_h, y_h = eval_position(h_idx, width)
        heatmap_data[y_h - 1, x_h - 1] = prob

    # 3. Plotting
    plt.figure(figsize=(8, 7))
    # 'YlOrRd' is a great color map for risk (Yellow to Red)
    ax = sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap='YlOrRd',
                     square=True, cbar_kws={'label': 'P(Infection)'})

    # Mark where the sick person is
    x_s, y_s = eval_position(s_idx, width)
    plt.scatter(x_s - 0.5, y_s - 0.5, marker='x', color='black', s=100, label='Sick Person Start')

    plt.title(f'Spatial Infection Risk after {time_steps} Minutes')
    plt.xlabel('Room X-Coordinate')
    plt.ylabel('Room Y-Coordinate')

    os.makedirs('static/images', exist_ok=True)
    plt.savefig('static/images/infection_heatmap.png', dpi=300)
    print("Success! Heat map saved to static/images/infection_heatmap.png")

def main():
    # Example: 9x9 room.
    # Sick person starts at Tile 3 (Left Wall).
    # Healthy person starts at Tile 40 (Center).
    prob = simulate_room(width=9, sick_start_tile_index=40, healthy_start_tile_index=40, time_steps=600)

    print(f"Probability of infection: {prob:.4f}")
    return 0


if __name__ == "__main__":
    generate_visual(width=9, s_idx=40, h_idx=40)