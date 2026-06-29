import pandas as pd

from factor_backtester.analytics.metrics import compute_wealth_index, drawdown_series
from factor_backtester.visualisation.plots import (
    plot_annual_returns,
    plot_cumulative_wealth,
    plot_drawdowns,
)


def main() -> None:
    momentum_returns = pd.read_csv(
        "data/processed/momentum_returns.csv",
        index_col=0,
        parse_dates=True,
    )["momentum_returns"]

    low_vol_returns = pd.read_csv(
        "data/processed/low_vol_returns.csv",
        index_col=0,
        parse_dates=True,
    )["low_vol_returns"]

    benchmark_returns = pd.read_csv(
        "data/processed/benchmark_returns.csv",
        index_col=0,
        parse_dates=True,
    )["SPY"]

    returns_df = pd.concat(
        [
            momentum_returns.rename("Momentum"),
            low_vol_returns.rename("Low Vol"),
            benchmark_returns.rename("SPY"),
        ],
        axis=1,
    )

    wealth_df = returns_df.apply(compute_wealth_index)
    drawdown_df = returns_df.apply(drawdown_series)

    plot_cumulative_wealth(
        wealth_df,
        title="Factor Strategies vs Benchmark: Cumulative Wealth",
        save_path="reports/figures/cumulative_wealth.png",
    )

    plot_drawdowns(
        drawdown_df,
        title="Factor Strategies vs Benchmark: Drawdowns",
        save_path="reports/figures/drawdowns.png",
    )

    plot_annual_returns(
        returns_df,
        title="Factor Strategies vs Benchmark: Annual Returns",
        save_path="reports/figures/annual_returns.png",
    )

    print("Report figures generated.")
    print("Saved files:")
    print("- reports/figures/cumulative_wealth.png")
    print("- reports/figures/drawdowns.png")
    print("- reports/figures/annual_returns.png")


if __name__ == "__main__":
    main()