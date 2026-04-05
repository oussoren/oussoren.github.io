import argparse
import time
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
import pyspiel

from open_spiel.python.pytorch.deep_cfr import DeepCFRSolver
from open_spiel.python.algorithms.exploitability import nash_conv
from open_spiel.python.bots.uniform_random import UniformRandomBot
from open_spiel.python.policy import Policy


class TorchPolicy(Policy):
    def __init__(self, game, policy_network: torch.nn.Module, device="cpu"):
        super().__init__(game, list(range(game.num_players())))
        self.game = game
        self.net = policy_network
        self.net.eval()
        self.device = device
        self.num_actions = game.num_distinct_actions()

    @torch.no_grad()
    def action_probabilities(self, state, player_id=None):
        if player_id is None:
            player_id = state.current_player()

        legal = state.legal_actions(player_id)

        info_state = state.information_state_tensor(player_id)
        x = torch.tensor(info_state, dtype=torch.float32, device=self.device).unsqueeze(0)  # (1, D)

        out = self.net(x)  # (1, A) or (A,)
        if out.dim() == 1:
            out = out.unsqueeze(0)

        out = out[:, : self.num_actions]
        vec = out.squeeze(0)

        # Heuristic: treat as probs if it's already in [0,1] and sums ~ 1.
        is_prob_like = False
        if torch.isfinite(vec).all() and torch.all(vec >= 0) and torch.all(vec <= 1.0):
            s = float(vec.sum().item())
            if abs(s - 1.0) < 1e-2:
                is_prob_like = True

        if is_prob_like:
            probs = vec
        else:
            # Mask illegal actions by setting logits very negative
            mask = torch.full((self.num_actions,), float("-inf"), device=self.device)
            mask[legal] = 0.0
            logits = vec + mask
            probs = F.softmax(logits, dim=-1)

        prob_dict = {a: float(probs[a].item()) for a in legal}
        z = sum(prob_dict.values())
        if not np.isfinite(z) or z <= 0:
            u = 1.0 / len(legal)
            prob_dict = {a: u for a in legal}
        else:
            prob_dict = {a: p / z for a, p in prob_dict.items()}
        return prob_dict


class PolicyBot(pyspiel.Bot):
    def __init__(self, player_id: int, policy: Policy, seed: int = 0):
        super().__init__()
        self.player_id = player_id
        self.policy = policy
        self.rng = np.random.RandomState(seed)

    def restart_at(self, state):
        return

    def step(self, state):
        legal = state.legal_actions(self.player_id)
        prob_dict = self.policy.action_probabilities(state, self.player_id)
        probs = np.array([prob_dict.get(a, 0.0) for a in legal], dtype=np.float64)
        s = probs.sum()
        if not np.isfinite(s) or s <= 0:
            probs = np.ones_like(probs) / len(probs)
        else:
            probs /= s
        return int(self.rng.choice(legal, p=probs))


def play_episode(game, bot0, bot1, seed=0):
    """Plays one full game and returns player 0 return."""
    rng = np.random.RandomState(seed)
    state = game.new_initial_state()

    while not state.is_terminal():
        if state.is_chance_node():
            outcomes = state.chance_outcomes()  # list[(action, prob)]
            actions, probs = zip(*outcomes)
            a = int(rng.choice(actions, p=probs))
            state.apply_action(a)
        else:
            p = state.current_player()
            if p == 0:
                a = bot0.step(state)
            else:
                a = bot1.step(state)
            state.apply_action(int(a))

    return float(state.returns()[0])


def eval_vs_uniform_random(game, policy, num_episodes=2000, seed=0):
    bot0 = PolicyBot(0, policy, seed=seed)
    bot1 = UniformRandomBot(1, np.random.RandomState(seed + 1))

    rets = []
    for i in range(num_episodes):
        rets.append(play_episode(game, bot0, bot1, seed=seed + 1000 + i))
    return float(np.mean(rets))


def train_and_eval(game_name: str, iterations: int, traversals: int, seed: int, num_eval_episodes: int, device="cpu"):
    np.random.seed(seed)
    torch.manual_seed(seed)

    game = pyspiel.load_game(game_name)

    solver = DeepCFRSolver(
        game=game,
        policy_network_layers=(256, 256),
        advantage_network_layers=(128, 128),
        num_iterations=iterations,
        num_traversals=traversals,
        learning_rate=1e-4,
        batch_size_advantage=None,
        batch_size_strategy=None,
        memory_capacity=1_000_000,
        policy_network_train_steps=1,
        advantage_network_train_steps=1,
        reinitialize_advantage_networks=True,
    )

    t0 = time.time()
    solver.solve()
    elapsed = time.time() - t0

    if not hasattr(solver, "_policy_network"):
        raise AttributeError("DeepCFRSolver missing _policy_network on this install.")

    pol = TorchPolicy(game, solver._policy_network, device=device)

    try:
        nc = float(nash_conv(game, pol))
    except Exception as e:
        nc = np.nan
        print(f"[warn] NashConv failed: {e}")

    try:
        ev = eval_vs_uniform_random(game, pol, num_episodes=num_eval_episodes, seed=seed + 12345)
    except Exception as e:
        ev = np.nan
        print(f"[warn] EV vs random failed: {e}")

    return nc, ev, elapsed


def run(game_name: str, iterations: int, traversals: int, seed: int, num_eval_episodes: int, curve_points: int, device="cpu"):
    print(f"Loaded game: {game_name}")
    rows = []

    if curve_points <= 1:
        nc, ev, elapsed = train_and_eval(game_name, iterations, traversals, seed, num_eval_episodes, device=device)
        print(f"FINAL | iters={iterations} | NashConv={nc:.4f} | EV vs random={ev:.4f} | wall={elapsed:.1f}s")
        rows.append({
            "game": game_name,
            "iteration": iterations,
            "nash_conv": nc,
            "ev_vs_uniform_random_p0": ev,
            "seed": seed,
            "traversals": traversals,
            "wall_time_sec": elapsed,
        })
    else:
        for k in range(1, curve_points + 1):
            it_k = int(round(iterations * k / curve_points))
            nc, ev, elapsed = train_and_eval(game_name, it_k, traversals, seed, num_eval_episodes, device=device)
            print(f"CURVE | iters={it_k:4d} | NashConv={nc:10.4f} | EV vs random={ev: .4f} | wall={elapsed: .1f}s")
            rows.append({
                "game": game_name,
                "iteration": it_k,
                "nash_conv": nc,
                "ev_vs_uniform_random_p0": ev,
                "seed": seed,
                "traversals": traversals,
                "wall_time_sec": elapsed,
            })

    df = pd.DataFrame(rows)
    out_csv = f"baseline_{game_name}_seed{seed}.csv".replace("/", "_")
    df.to_csv(out_csv, index=False)
    print(f"\nSaved: {out_csv}")
    print(df.tail(min(8, len(df))).to_string(index=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--game", type=str, default="kuhn_poker", choices=["kuhn_poker", "leduc_poker"])
    parser.add_argument("--iterations", type=int, default=200)
    parser.add_argument("--traversals", type=int, default=200)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--num_eval_episodes", type=int, default=2000)
    parser.add_argument("--curve_points", type=int, default=1)
    parser.add_argument("--device", type=str, default="cpu")
    args = parser.parse_args()

    run(
        game_name=args.game,
        iterations=args.iterations,
        traversals=args.traversals,
        seed=args.seed,
        num_eval_episodes=args.num_eval_episodes,
        curve_points=args.curve_points,
        device=args.device,
    )