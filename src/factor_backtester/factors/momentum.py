import pandas as pd


def compute_momentum_signal(
    prices: pd.DataFrame,
    lookback: int = 252,
    skip: int = 21,
) -> pd.DataFrame:
    """
    Compute cross-sectional momentum signal using a lookback window
    and a skip window.

    Signal at date t is approximately:
        prices.shift(skip) / prices.shift(lookback) - 1
    """
    signal = prices.shift(skip) / prices.shift(lookback) - 1
    return signal