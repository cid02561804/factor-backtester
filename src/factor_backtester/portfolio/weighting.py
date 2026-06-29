import pandas as pd


def equal_weight_portfolio(selection: pd.DataFrame) -> pd.DataFrame:
    """
    Convert a boolean selection matrix into equal weights across selected assets.
    """
    weights = selection.astype(float)
    row_sums = weights.sum(axis=1)

    weights = weights.div(row_sums.replace(0, pd.NA), axis=0)
    weights = weights.fillna(0.0)

    return weights