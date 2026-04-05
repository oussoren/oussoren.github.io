import argparse
import time
import numpy as np
import pandas as pd
import torch
import pyspiel

from open_spiel.python.algorithms.exploitability import nash_conv
from open_spiel.python.pytorch.deep_cfr import DeepCFRSolver

from entropy_deep_cfr import EntropyDeepCFRSolver
from run_baseline_deepcfr import TorchPolicy, eval_vs_uniform_random


def train_one(game_name, iterations, traversals, seed, alpha, num_eval_episodes, device="cpu"):
    np.random.seed(seed)
    torch.manual_seed(seed)

    game = pyspiel.load_game(game_name)

    Solver = DeepCFRSolver if alpha == 0.0 else EntropyDeepCFRSolver

    kwargs = dict(
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
    if alpha != 0.0:
        kwargs["alpha"] = alpha

    solver = Solver(**kwargs)

    t0 = time.time()
    solver.solve()
    wall = time.time() - t0

    pol = TorchPolicy(game, solver._policy_network, device=device)

    nc = float(nash_conv(game, pol))
    ev = float(eval_vs_uniform_random(game, pol, num_episodes=num_eval_episodes, seed=seed + 999))

    return nc, ev, wall


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--game", type=str, default="kuhn_poker", choices=["kuhn_poker", "leduc_poker"])
    parser.add_argument("--iterations", type=int, default=200)
    parser.add_argument("--traversals", type=int, default=200)
    parser.add_argument("--num_eval_episodes", type=int, default=2000)
    parser.add_argument("--seeds", type=str, default="0,1,2")
    parser.add_argument("--alphas", type=str, default="0,0.1,1,5")
    parser.add_argument("--device", type=str, default="cpu")
    args = parser.parse_args()

    seeds = [int(x) for x in args.seeds.split(",")]
    alphas = [float(x) for x in args.alphas.split(",")]

    rows = []
    for seed in seeds:
        for alpha in alphas:
            print(f"\n=== {args.game} | seed={seed} | alpha={alpha} ===")
            nc, ev, wall = train_one(
                args.game, args.iterations, args.traversals, seed, alpha, args.num_eval_episodes, device=args.device
            )
            print(f"RESULT | NashConv={nc:.4f} | EVvsRand={ev:.4f} | wall={wall:.1f}s")

            rows.append({
                "game": args.game,
                "seed": seed,
                "alpha": alpha,
                "iterations": args.iterations,
                "traversals": args.traversals,
                "nash_conv": nc,
                "ev_vs_uniform_random_p0": ev,
                "wall_time_sec": wall,
            })

    df = pd.DataFrame(rows)
    out = f"sweep_{args.game}_iters{args.iterations}_trav{args.traversals}.csv".replace("/", "_")
    df.to_csv(out, index=False)
    print(f"\nSaved: {out}")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()