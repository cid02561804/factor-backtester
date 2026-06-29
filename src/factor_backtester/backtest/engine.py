import pandas as pd

from factor_backtester.analytics.returns import compute_cumulative_wealth


def backtest_from_weights(
    asset_returns: pd.DataFrame,
    weights: pd.DataFrame,
) -> tuple[pd.Series, pd.Series]:
    """
    Backtest a portfolio from asset returns and time-varying weights.

    Weights are assumed to be decided at rebalance dates and are shifted
    forward by one trading day before being applied to returns.
    """
    aligned_weights = weights.reindex(asset_returns.index).ffill().fillna(0.0)
    shifted_weights = aligned_weights.shift(1).fillna(0.0)

    portfolio_returns = (shifted_weights * asset_returns).sum(axis=1)
    portfolio_wealth = compute_cumulative_wealth(portfolio_returns)

    return portfolio_returns, portfolio_wealth