import argparse
import time
import numpy as np
import pandas as pd
import torch
import pyspiel
import inspect

from run_baseline_deepcfr import TorchPolicy, PolicyBot, play_episode
from open_spiel.python.pytorch.deep_cfr import DeepCFRSolver
from soft_rm_deep_cfr import SoftRegretMatchingDeepCFRSolver


def _find_solver_class(mod):
    candidates = []
    for name in dir(mod):
        obj = getattr(mod, name)
        if not inspect.isclass(obj):
            continue
        if "Test" in name or "test" in name:
            continue
        if not any(k in name for k in ["MCCFR", "CFR", "Outcome", "External", "Solver"]):
            continue
        has_iter = any(hasattr(obj, m) for m in ["iteration", "run_iteration", "execute_iteration", "step"])
        if not has_iter:
            continue
        candidates.append((name, obj))
    candidates.sort(key=lambda x: ("MCCFR" not in x[0], "Solver" not in x[0], x[0]))
    return candidates[0][1] if candidates else None


def make_mccfr_solver(game):
    errors = []
    try:
        from open_spiel.python.algorithms import outcome_sampling_mccfr as osm
        cls = _find_solver_class(osm)
        if cls is None:
            raise ImportError("No suitable solver class found in outcome_sampling_mccfr.")
        return cls(game)
    except Exception as e:
        errors.append(("outcome_sampling_mccfr", str(e)))

    try:
        from open_spiel.python.algorithms import external_sampling_mccfr as esm
        cls = _find_solver_class(esm)
        if cls is None:
            raise ImportError("No suitable solver class found in external_sampling_mccfr.")
        return cls(game)
    except Exception as e:
        errors.append(("external_sampling_mccfr", str(e)))

    raise ImportError("Could not construct MCCFR solver: " + str(errors))


def mccfr_step(solver):
    for name in ["iteration", "run_iteration", "execute_iteration", "step"]:
        if hasattr(solver, name) and callable(getattr(solver, name)):
            return getattr(solver, name)()
    raise AttributeError("No iteration method on MCCFR solver.")


def get_mccfr_average_policy(solver):
    for name in ["average_policy", "get_average_policy", "average_strategy", "get_average_strategy"]:
        if hasattr(solver, name) and callable(getattr(solver, name)):
            return getattr(solver, name)()
    for name in ["policy", "average_policy", "_average_policy", "_policy"]:
        if hasattr(solver, name):
            obj = getattr(solver, name)
            if callable(obj):
                try:
                    return obj()
                except TypeError:
                    pass
            else:
                return obj
    raise AttributeError("Could not obtain average policy from MCCFR solver.")


def train_mccfr_policy(game_name: str, iterations: int, seed: int = 0):
    np.random.seed(seed)
    game = pyspiel.load_game(game_name)
    solver = make_mccfr_solver(game)
    t0 = time.time()
    for _ in range(iterations):
        mccfr_step(solver)
    wall = time.time() - t0
    pol = get_mccfr_average_policy(solver)
    return game, pol, wall


def train_deepcfr_policy(game_name: str, iterations: int, traversals: int, seed: int, rm_lambda, device="cpu"):
    np.random.seed(seed)
    torch.manual_seed(seed)
    game = pyspiel.load_game(game_name)

    if rm_lambda is None:
        Solver = DeepCFRSolver
        kwargs = {}
    else:
        Solver = SoftRegretMatchingDeepCFRSolver
        kwargs = {"rm_lambda": float(rm_lambda)}

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

    t0 = time.time()
    solver.solve()
    wall = time.time() - t0

    pol = TorchPolicy(game, solver._policy_network, device=device)
    return game, pol, wall


def eval_policy_vs_policy(game, p0_policy, p1_policy, num_episodes=3000, seed=0):
    bot0 = PolicyBot(0, p0_policy, seed=seed + 1)
    bot1 = PolicyBot(1, p1_policy, seed=seed + 2)
    rets = []
    for i in range(num_episodes):
        rets.append(play_episode(game, bot0, bot1, seed=seed + 1000 + i))
    return float(np.mean(rets))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--game", type=str, default="kuhn_poker", choices=["kuhn_poker", "leduc_poker"])
    parser.add_argument("--deepcfr_iterations", type=int, default=500)
    parser.add_argument("--deepcfr_traversals", type=int, default=200)
    parser.add_argument("--rm_lambdas", type=str, default="baseline,0.1,0.3,1.0")
    parser.add_argument("--mccfr_iters", type=str, default="5000,20000")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--num_episodes", type=int, default=3000)
    parser.add_argument("--device", type=str, default="cpu")
    args = parser.parse_args()

    rm_lams = []
    for x in args.rm_lambdas.split(","):
        if x.strip().lower() == "baseline":
            rm_lams.append(None)
        else:
            rm_lams.append(float(x))

    mccfr_iters = [int(x) for x in args.mccfr_iters.split(",")]

    opponents = []
    for it in mccfr_iters:
        print(f"\n=== Training MCCFR opponent: iters={it} ===")
        game, opp_pol, wall = train_mccfr_policy(args.game, it, seed=args.seed + 17 * it)
        print(f"MCCFR trained | iters={it} | wall={wall:.2f}s")
        opponents.append((it, opp_pol, wall))

    rows = []
    for lam in rm_lams:
        name = "baseline" if lam is None else str(lam)
        print(f"\n=== Training DeepCFR model: rm_lambda={name} ===")
        game, pol, wall = train_deepcfr_policy(
            args.game, args.deepcfr_iterations, args.deepcfr_traversals, args.seed, lam, device=args.device
        )
        print(f"DeepCFR trained | rm_lambda={name} | wall={wall:.2f}s")

        for (opp_it, opp_pol, opp_wall) in opponents:
            ev = eval_policy_vs_policy(game, pol, opp_pol, num_episodes=args.num_episodes, seed=args.seed + 777 + opp_it)
            print(f"rm_lambda={name:>8} vs MCCFR({opp_it}) | EV={ev:.4f}")
            rows.append({
                "game": args.game,
                "seed": args.seed,
                "rm_lambda": name,
                "deepcfr_iterations": args.deepcfr_iterations,
                "deepcfr_traversals": args.deepcfr_traversals,
                "mccfr_iterations": opp_it,
                "ev_p0_vs_mccfr": ev,
                "num_episodes": args.num_episodes,
                "wall_deepcfr_sec": wall,
                "wall_mccfr_sec": opp_wall,
            })

    df = pd.DataFrame(rows)
    out = f"crossplay_mccfr_softrm_{args.game}_seed{args.seed}_deep{args.deepcfr_iterations}_trav{args.deepcfr_traversals}.csv".replace("/", "_")
    df.to_csv(out, index=False)
    print(f"\nSaved: {out}")
    print(df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()