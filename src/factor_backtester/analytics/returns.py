import pandas as pd


def compute_simple_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Compute simple returns from price data.
    """
    returns = prices.pct_change()
    return returns


def compute_cumulative_wealth(returns: pd.Series, initial_value: float = 1.0) -> pd.Series:
    """
    Compute cumulative wealth index from a return series.
    """
    wealth = initial_value * (1 + returns.fillna(0)).cumprod()
    return wealth