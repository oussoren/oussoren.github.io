import argparse
import numpy as np
import pandas as pd
import torch
import pyspiel

from open_spiel.python.pytorch.deep_cfr import DeepCFRSolver
from entropy_deep_cfr import EntropyDeepCFRSolver
from run_baseline_deepcfr import TorchPolicy, PolicyBot, play_episode
from open_spiel.python.bots.uniform_random import UniformRandomBot


class MixtureBot(pyspiel.Bot):
    def __init__(self, player_id, policy, eps, seed=0):
        super().__init__()
        self.player_id = player_id
        self.policy_bot = PolicyBot(player_id, policy, seed=seed)
        self.rand_bot = UniformRandomBot(player_id, np.random.RandomState(seed + 1))
        self.eps = float(eps)
        self.rng = np.random.RandomState(seed + 2)

    def restart_at(self, state):
        return

    def step(self, state):
        if self.rng.rand() < self.eps:
            return self.rand_bot.step(state)
        return self.policy_bot.step(state)


def eval_vs_bot(game, bot0, bot1, num_episodes=10000, seed=0):
    rets = []
    for i in range(num_episodes):
        rets.append(play_episode(game, bot0, bot1, seed=seed + i))
    return float(np.mean(rets))


def train_policy(game_name, iterations, traversals, seed, alpha, device="cpu"):
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
    solver.solve()

    pol = TorchPolicy(game, solver._policy_network, device=device)
    return game, pol


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--game", type=str, default="kuhn_poker", choices=["kuhn_poker", "leduc_poker"])
    parser.add_argument("--iterations", type=int, default=200)
    parser.add_argument("--traversals", type=int, default=200)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--alphas", type=str, default="0,0.5,1,2")
    parser.add_argument("--epsilons", type=str, default="0,0.1,0.2,0.3,0.5")
    parser.add_argument("--num_episodes", type=int, default=10000)
    parser.add_argument("--device", type=str, default="cpu")
    args = parser.parse_args()

    alphas = [float(x) for x in args.alphas.split(",")]
    epsilons = [float(x) for x in args.epsilons.split(",")]

    game, baseline_pol = train_policy(args.game, args.iterations, args.traversals, args.seed, alpha=0.0, device=args.device)

    rows = []

    for alpha in alphas:
        print(f"\n=== Training alpha={alpha} ===")
        game, pol = train_policy(args.game, args.iterations, args.traversals, args.seed, alpha=alpha, device=args.device)

        bot0 = PolicyBot(0, pol, seed=args.seed + 10)

        for eps in epsilons:
            opp = MixtureBot(1, baseline_pol, eps=eps, seed=args.seed + 100)
            ev = eval_vs_bot(game, bot0, opp, num_episodes=args.num_episodes, seed=args.seed + 1000)
            print(f"alpha={alpha:>4} | eps={eps:.2f} | EV={ev:.4f}")

            rows.append({
                "game": args.game,
                "seed": args.seed,
                "iterations": args.iterations,
                "traversals": args.traversals,
                "alpha": alpha,
                "epsilon": eps,
                "ev_vs_mixture_baseline_uniform": ev,
                "num_episodes": args.num_episodes,
            })

    df = pd.DataFrame(rows)
    out = f"noise_curve_{args.game}_seed{args.seed}_iters{args.iterations}_trav{args.traversals}.csv".replace("/", "_")
    df.to_csv(out, index=False)
    print(f"\nSaved: {out}")
    print(df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()