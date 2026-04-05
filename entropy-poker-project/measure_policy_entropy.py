import argparse
import numpy as np
import pandas as pd
import torch
import pyspiel

from run_baseline_deepcfr import TorchPolicy, PolicyBot, play_episode
from open_spiel.python.pytorch.deep_cfr import DeepCFRSolver
from entropy_deep_cfr import EntropyDeepCFRSolver
from soft_rm_deep_cfr import SoftRegretMatchingDeepCFRSolver


def sample_states(game, num_episodes=200, seed=0):
    rng = np.random.RandomState(seed)
    states = []
    for ep in range(num_episodes):
        s = game.new_initial_state()
        while not s.is_terminal():
            if s.is_chance_node():
                outcomes = s.chance_outcomes()
                actions, probs = zip(*outcomes)
                a = int(rng.choice(actions, p=probs))
                s.apply_action(a)
            else:
                # record decision state
                states.append(s.clone())
                p = s.current_player()
                a = int(rng.choice(s.legal_actions(p)))
                s.apply_action(a)
    return states


def entropy_of_policy_on_states(policy, states, player_id=0, eps=1e-12):
    ents = []
    for st in states:
        if st.is_terminal() or st.is_chance_node():
            continue
        p = st.current_player()
        if p != player_id:
            continue
        probs = policy.action_probabilities(st, p)
        ps = np.array(list(probs.values()), dtype=np.float64)
        ps = np.clip(ps, eps, 1.0)
        ps = ps / ps.sum()
        ents.append(float(-(ps * np.log(ps)).sum()))
    return float(np.mean(ents)) if ents else float("nan")


def train_policy(game_name, iterations, traversals, seed, mode, alpha, rm_lambda, device="cpu"):
    np.random.seed(seed)
    torch.manual_seed(seed)
    game = pyspiel.load_game(game_name)

    if mode == "baseline":
        Solver = DeepCFRSolver
        kwargs = {}
    elif mode == "entropy":
        Solver = EntropyDeepCFRSolver
        kwargs = {"alpha": float(alpha)}
    elif mode == "softrm":
        Solver = SoftRegretMatchingDeepCFRSolver
        kwargs = {"rm_lambda": float(rm_lambda)}
    else:
        raise ValueError("mode must be baseline|entropy|softrm")

    solver = Solver(
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
        **kwargs
    )
    solver.solve()
    pol = TorchPolicy(game, solver._policy_network, device=device)
    return game, pol


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", type=str, default="kuhn_poker", choices=["kuhn_poker", "leduc_poker"])
    ap.add_argument("--iterations", type=int, default=200)
    ap.add_argument("--traversals", type=int, default=200)
    ap.add_argument("--seeds", type=str, default="0,1,2")
    ap.add_argument("--device", type=str, default="cpu")
    args = ap.parse_args()

    seeds = [int(x) for x in args.seeds.split(",")]

    configs = [
        ("baseline", None, None),
        ("entropy", 1.0, None),
        ("softrm", None, 0.1),
        ("softrm", None, 0.3),
    ]

    rows = []
    for seed in seeds:
        game = pyspiel.load_game(args.game)
        states = sample_states(game, num_episodes=200, seed=seed + 999)

        for mode, alpha, rm_lambda in configs:
            game2, pol = train_policy(
                args.game, args.iterations, args.traversals, seed,
                mode=mode, alpha=alpha, rm_lambda=rm_lambda, device=args.device
            )
            ent = entropy_of_policy_on_states(pol, states, player_id=0)
            rows.append({
                "game": args.game,
                "seed": seed,
                "mode": mode,
                "alpha": alpha,
                "rm_lambda": rm_lambda,
                "mean_action_entropy_p0": ent,
                "iterations": args.iterations,
                "traversals": args.traversals,
                "num_states": len(states),
            })
            print(rows[-1])

    df = pd.DataFrame(rows)
    out = f"policy_entropy_{args.game}_iters{args.iterations}_trav{args.traversals}.csv".replace("/", "_")
    df.to_csv(out, index=False)
    print("\nSaved:", out)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()