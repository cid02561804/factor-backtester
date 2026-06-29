import pandas as pd


def get_monthly_rebalance_dates(index: pd.DatetimeIndex) -> pd.DatetimeIndex:
    """
    Return the last available trading date of each month from a DatetimeIndex.
    """
    dates = pd.Series(index=index, data=index)
    rebalance_dates = dates.groupby(index.to_period("M")).max()
    return pd.DatetimeIndex(rebalance_dates.values)