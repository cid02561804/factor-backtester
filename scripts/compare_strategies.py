import pandas as pd

from factor_backtester.analytics.metrics import performance_summary


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

    summaries = pd.DataFrame(
        [
            performance_summary(momentum_returns, name="momentum"),
            performance_summary(low_vol_returns, name="low_vol"),
            performance_summary(benchmark_returns, name="SPY"),
        ]
    )

    print("Performance summary:")
    print(summaries)

    summaries.to_csv("data/processed/performance_summary.csv", index=False)


if __name__ == "__main__":
    main()