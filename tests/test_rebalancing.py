import pandas as pd

from factor_backtester.portfolio.rebalancing import get_monthly_rebalance_dates
from factor_backtester.portfolio.weighting import equal_weight_portfolio


def test_get_monthly_rebalance_dates_returns_month_end_dates():
    index = pd.to_datetime([
        "2024-01-30", "2024-01-31",
        "2024-02-27", "2024-02-29",
        "2024-03-28",
    ])

    rebalance_dates = get_monthly_rebalance_dates(index)

    expected = pd.to_datetime([
        "2024-01-31",
        "2024-02-29",
        "2024-03-28",
    ])

    assert list(rebalance_dates) == list(expected)


def test_equal_weight_portfolio_sums_to_one_when_assets_selected():
    selection = pd.DataFrame(
        {
            "A": [True, False],
            "B": [True, False],
            "C": [False, False],
        },
        index=pd.to_datetime(["2024-01-31", "2024-02-29"]),
    )

    weights = equal_weight_portfolio(selection)

    assert weights.loc["2024-01-31"].sum() == 1.0
    assert weights.loc["2024-01-31", "A"] == 0.5
    assert weights.loc["2024-01-31", "B"] == 0.5
    assert weights.loc["2024-02-29"].sum() == 0.0