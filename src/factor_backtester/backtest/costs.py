import pandas as pd


def compute_turnover(weights: pd.DataFrame) -> pd.Series:
    """
    Compute portfolio turnover from a DataFrame of target weights.
    Turnover is 0.5 * sum(abs(delta weights)) across assets.
    """
    weight_changes = weights.fillna(0.0).diff().fillna(weights.fillna(0.0))
    turnover = 0.5 * weight_changes.abs().sum(axis=1)
    return turnover


def transaction_costs_from_turnover(
    turnover: pd.Series,
    cost_bps: float = 10.0,
) -> pd.Series:
    """
    Convert turnover into transaction cost series.

    Parameters
    ----------
    turnover : pd.Series
        Turnover series.
    cost_bps : float
        Cost per unit turnover in basis points.
    """
    cost_rate = cost_bps / 10000.0
    return turnover * cost_rate


def apply_transaction_costs(
    gross_returns: pd.Series,
    costs: pd.Series,
) -> pd.Series:
    """
    Subtract transaction costs from gross portfolio returns.
    """
    aligned_costs = costs.reindex(gross_returns.index).fillna(0.0)
    net_returns = gross_returns - aligned_costs
    return net_returns