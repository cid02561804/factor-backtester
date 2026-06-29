import pandas as pd


def validate_price_data(prices: pd.DataFrame) -> dict:
    """
    Run basic validation checks on a price DataFrame.
    """
    return {
        "shape": prices.shape,
        "duplicate_dates": int(prices.index.duplicated().sum()),
        "missing_values": int(prices.isna().sum().sum()),
        "empty_columns": prices.columns[prices.isna().all()].tolist(),
        "start_date": prices.index.min(),
        "end_date": prices.index.max(),
    }