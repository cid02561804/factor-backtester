import pandas as pd


def compute_low_vol_signal(
    returns: pd.DataFrame,
    window: int = 63,
) -> pd.DataFrame:
    """
    Compute trailing rolling volatility signal from asset returns.

    Lower values indicate lower historical volatility.
    """
    signal = returns.rolling(window=window).std()
    return signal