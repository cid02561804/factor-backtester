import pandas as pd


def compute_eligibility_mask(
    prices: pd.DataFrame,
    min_history: int = 252,
) -> pd.DataFrame:
    """
    Compute a boolean eligibility mask indicating whether each asset
    has at least `min_history` valid observations up to each date.
    """
    valid_obs = prices.notna().cumsum()
    eligibility = valid_obs >= min_history
    return eligibility