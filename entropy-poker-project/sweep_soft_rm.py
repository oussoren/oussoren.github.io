import argparse
import time
import numpy as np
import pandas as pd
import torch
import pyspiel

from open_spiel.python.algorithms.exploitability import nash_conv
from run_baseline_deepcfr import TorchPolicy, eval_vs_uniform_random
from open_spiel.python.pytorch.deep_cfr import DeepCFRSolver
from soft_rm_deep_cfr import SoftRegretMatchingDeepCFRSolver


def train_one(game_name, iterations, traversals, seed, rm_lambda, num_eval_episodes, device="cpu"):
    np.random.seed(seed)
    torch.manual_seed(seed)
    game = pyspiel.load_game(game_name)

    Solver = DeepCFRSolver if rm_lambda is None else SoftRegretMatchingDeepCFRSolver

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
    if rm_lambda is not None:
        kwargs["rm_lambda"] = float(rm_lambda)

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
    parser.add_argument("--lambdas", type=str, default="baseline,0.1,0.3,1,3,10")
    parser.add_argument("--device", type=str, default="cpu")
    args = parser.parse_args()

    seeds = [int(x) for x in args.seeds.split(",")]
    lambdas = []
    for x in args.lambdas.split(","):
        if x.strip().lower() == "baseline":
            lambdas.append(None)
        else:
            lambdas.append(float(x))

    rows = []
    for seed in seeds:
        for lam in lambdas:
            name = "baseline" if lam is None else f"{lam}"
            print(f"\n=== game={args.game} seed={seed} rm_lambda={name} ===")
            nc, ev, wall = train_one(args.game, args.iterations, args.traversals, seed, lam, args.num_eval_episodes, device=args.device)
            print(f"RESULT | NashConv={nc:.4f} | EVvsRand={ev:.4f} | wall={wall:.1f}s")
            rows.append({
                "game": args.game,
                "seed": seed,
                "rm_lambda": name,
                "iterations": args.iterations,
                "traversals": args.traversals,
                "nash_conv": nc,
                "ev_vs_uniform_random_p0": ev,
                "wall_time_sec": wall,
            })

    df = pd.DataFrame(rows)
    out = f"sweep_softrm_{args.game}_iters{args.iterations}_trav{args.traversals}.csv".replace("/", "_")
    df.to_csv(out, index=False)
    print(f"\nSaved: {out}")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()