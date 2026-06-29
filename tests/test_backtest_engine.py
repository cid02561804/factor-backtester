import numpy as np
import pandas as pd

from factor_backtester.backtest.engine import backtest_from_weights


def test_backtest_from_weights_applies_one_day_shift():
    asset_returns = pd.DataFrame(
        {
            "A": [0.01, 0.02, 0.03],
            "B": [0.00, 0.00, 0.00],
        },
        index=pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
    )

    weights = pd.DataFrame(
        {
            "A": [1.0, 1.0, 1.0],
            "B": [0.0, 0.0, 0.0],
        },
        index=asset_returns.index,
    )

    portfolio_returns, _ = backtest_from_weights(asset_returns, weights)

    assert np.isclose(portfolio_returns.iloc[0], 0.0)
    assert np.isclose(portfolio_returns.iloc[1], 0.02)
    assert np.isclose(portfolio_returns.iloc[2], 0.03)