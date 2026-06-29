from factor_backtester.data.loaders import download_adjusted_close
from factor_backtester.utils.validation import validate_price_data
from factor_backtester.data.cleaning import load_and_clean_prices, save_processed_prices
from factor_backtester.data.universe import compute_eligibility_mask


TICKERS = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "META", "NVDA", "JPM", "JNJ", "XOM", "PG",
    "HD", "CVX", "LLY", "ABBV", "PEP", "KO", "MRK", "COST", "AVGO", "WMT",
]

BENCHMARK = ["SPY"]


def main() -> None:
    tickers = TICKERS + BENCHMARK

    prices = download_adjusted_close(
        tickers=tickers,
        start="2015-01-01",
        end="2026-01-01",
        save_path="data/raw/prices.csv",
    )

    summary = validate_price_data(prices)

    print("Download complete.")
    print("Validation summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

def main() -> None:
    prices = load_and_clean_prices("data/raw/prices.csv")
    eligibility = compute_eligibility_mask(prices, min_history=252)

    save_processed_prices(prices, "data/processed/prices_clean.csv")
    save_processed_prices(eligibility.astype(int), "data/processed/eligibility_mask.csv")

    print("Processed data saved.")
    print(f"Clean prices shape: {prices.shape}")
    print(f"Eligibility mask shape: {eligibility.shape}")
    print("Latest eligible asset counts:")
    print(eligibility.sum(axis=1).tail())


if __name__ == "__main__":
    main()