import numpy as np
import pandas as pd

from factor_backtester.analytics.metrics import (
    compute_wealth_index,
    drawdown_series,
    max_drawdown,
)


def test_compute_wealth_index_simple_case():
    returns = pd.Series([0.10, -0.10], index=pd.to_datetime(["2024-01-01", "2024-01-02"]))
    wealth = compute_wealth_index(returns, initial_value=1.0)

    assert np.isclose(wealth.iloc[0], 1.10)
    assert np.isclose(wealth.iloc[1], 0.99)


def test_drawdown_series_simple_case():
    returns = pd.Series([0.10, -0.20], index=pd.to_datetime(["2024-01-01", "2024-01-02"]))
    drawdowns = drawdown_series(returns)

    assert np.isclose(drawdowns.iloc[0], 0.0)
    assert np.isclose(drawdowns.iloc[1], -0.20)


def test_max_drawdown_simple_case():
    returns = pd.Series([0.10, -0.20], index=pd.to_datetime(["2024-01-01", "2024-01-02"]))
    mdd = max_drawdown(returns)

    assert np.isclose(mdd, -0.20)