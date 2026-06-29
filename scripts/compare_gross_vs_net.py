import pandas as pd

from factor_backtester.analytics.metrics import performance_summary


def main() -> None:
    momentum_gross = pd.read_csv(
        "data/processed/momentum_gross_returns.csv",
        index_col=0,
        parse_dates=True,
    )["momentum_gross_returns"]

    momentum_net = pd.read_csv(
        "data/processed/momentum_net_returns.csv",
        index_col=0,
        parse_dates=True,
    )["momentum_net_returns"]

    low_vol_gross = pd.read_csv(
        "data/processed/low_vol_gross_returns.csv",
        index_col=0,
        parse_dates=True,
    )["low_vol_gross_returns"]

    low_vol_net = pd.read_csv(
        "data/processed/low_vol_net_returns.csv",
        index_col=0,
        parse_dates=True,
    )["low_vol_net_returns"]

    summary = pd.DataFrame(
        [
            performance_summary(momentum_gross, name="momentum_gross"),
            performance_summary(momentum_net, name="momentum_net"),
            performance_summary(low_vol_gross, name="low_vol_gross"),
            performance_summary(low_vol_net, name="low_vol_net"),
        ]
    )

    print("Gross vs Net Performance Summary:")
    print(summary)

    summary.to_csv("data/processed/gross_vs_net_summary.csv", index=False)


if __name__ == "__main__":
    main()