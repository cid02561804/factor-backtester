import pandas as pd


def select_top_n(
    scores: pd.DataFrame,
    eligibility: pd.DataFrame,
    n: int,
) -> pd.DataFrame:
    """
    Select the top-n eligible assets by score at each date.

    Returns a boolean DataFrame with the same shape as scores.
    """
    if scores.shape != eligibility.shape:
        raise ValueError("Scores and eligibility must have the same shape.")

    masked_scores = scores.where(eligibility)

    selection = pd.DataFrame(False, index=scores.index, columns=scores.columns)

    for date in scores.index:
        row = masked_scores.loc[date].dropna()
        top_assets = row.nlargest(n).index
        selection.loc[date, top_assets] = True

    return selection

def select_bottom_n(
    scores: pd.DataFrame,
    eligibility: pd.DataFrame,
    n: int,
) -> pd.DataFrame:
    """
    Select the bottom-n eligible assets by score at each date.

    Returns a boolean DataFrame with the same shape as scores.
    """
    if scores.shape != eligibility.shape:
        raise ValueError("Scores and eligibility must have the same shape.")

    masked_scores = scores.where(eligibility)

    selection = pd.DataFrame(False, index=scores.index, columns=scores.columns)

    for date in scores.index:
        row = masked_scores.loc[date].dropna()
        bottom_assets = row.nsmallest(n).index
        selection.loc[date, bottom_assets] = True

    return selection