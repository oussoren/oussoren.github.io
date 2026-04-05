import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_crossplay(pattern):
    files = sorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError(f"No files matched: {pattern}")
    dfs = [pd.read_csv(f) for f in files]
    df = pd.concat(dfs, ignore_index=True)
    return df, files

def plot_ev_vs_mccfr(df, outpath="ev_vs_mccfr_strength.png"):
    # Ensure types
    df["mccfr_iterations"] = df["mccfr_iterations"].astype(int)
    df["ev_p0_vs_mccfr"] = df["ev_p0_vs_mccfr"].astype(float)

    agg = (
        df.groupby(["rm_lambda", "mccfr_iterations"])["ev_p0_vs_mccfr"]
          .agg(["mean", "std", "count"])
          .reset_index()
          .sort_values(["rm_lambda", "mccfr_iterations"])
    )

    plt.figure()
    for rm in agg["rm_lambda"].unique():
        sub = agg[agg["rm_lambda"] == rm].sort_values("mccfr_iterations")
        x = sub["mccfr_iterations"].values
        y = sub["mean"].values
        yerr = sub["std"].fillna(0.0).values
        plt.errorbar(x, y, yerr=yerr, marker="o", capsize=3, label=f"rm_lambda={rm}")

    plt.xscale("log")
    plt.xlabel("MCCFR opponent iterations (log scale)")
    plt.ylabel("EV (P0) vs MCCFR opponent")
    plt.title("Kuhn: DeepCFR vs MCCFR ladder (mean ± std over seeds)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath, dpi=200)
    print("Saved", outpath)

def main():
    df, files = load_crossplay("crossplay_mccfr_softrm_kuhn_poker_seed*_deep500_trav200.csv")
    print("Loaded files:")
    for f in files:
        print(" -", f)
    plot_ev_vs_mccfr(df)

if __name__ == "__main__":
    main()