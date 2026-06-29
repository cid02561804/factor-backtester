from pathlib import Path
import pandas as pd


def load_and_clean_prices(file_path: str) -> pd.DataFrame:
    """
    Load raw price data from CSV and apply basic cleaning steps.
    """
    prices = pd.read_csv(file_path, index_col=0, parse_dates=True)

    prices = prices.sort_index()
    prices = prices[~prices.index.duplicated(keep="first")]

    prices = prices.dropna(axis=1, how="all")

    return prices


def save_processed_prices(prices: pd.DataFrame, save_path: str) -> None:
    """
    Save cleaned price data to CSV.
    """
    save_file = Path(save_path)
    save_file.parent.mkdir(parents=True, exist_ok=True)
    prices.to_csv(save_file)