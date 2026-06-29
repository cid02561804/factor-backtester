from pathlib import Path
import pandas as pd
import yfinance as yf


def download_adjusted_close(
    tickers: list[str],
    start: str,
    end: str,
    save_path: str | None = None,
) -> pd.DataFrame:
    """
    Download adjusted close prices for a list of tickers.

    Parameters
    ----------
    tickers : list[str]
        List of ticker symbols.
    start : str
        Start date in YYYY-MM-DD format.
    end : str
        End date in YYYY-MM-DD format.
    save_path : str | None
        Optional file path for saving the downloaded prices as CSV.

    Returns
    -------
    pd.DataFrame
        DataFrame of adjusted close prices with dates as index and tickers as columns.
    """
    data = yf.download(
        tickers=tickers,
        start=start,
        end=end,
        auto_adjust=False,
        progress=False,
    )

    if "Adj Close" not in data:
        raise ValueError("Adjusted close data not found in downloaded dataset.")

    prices = data["Adj Close"].copy()
    prices = prices.sort_index()

    if isinstance(prices, pd.Series):
        prices = prices.to_frame()

    if save_path is not None:
        save_file = Path(save_path)
        save_file.parent.mkdir(parents=True, exist_ok=True)
        prices.to_csv(save_file)

    return prices