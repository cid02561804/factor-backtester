from factor_backtester.analytics.returns import compute_simple_returns, compute_cumulative_wealth
from factor_backtester.backtest.benchmark import split_assets_and_benchmark
from factor_backtester.data.cleaning import load_and_clean_prices, save_processed_prices


def main() -> None:
    prices = load_and_clean_prices("data/processed/prices_clean.csv")
    returns = compute_simple_returns(prices)

    asset_returns, benchmark_returns = split_assets_and_benchmark(returns, benchmark_col="SPY")
    benchmark_wealth = compute_cumulative_wealth(benchmark_returns)

    save_processed_prices(returns, "data/processed/returns.csv")
    save_processed_prices(asset_returns, "data/processed/asset_returns.csv")
    save_processed_prices(benchmark_returns.to_frame(name="SPY"), "data/processed/benchmark_returns.csv")
    save_processed_prices(benchmark_wealth.to_frame(name="SPY_wealth"), "data/processed/benchmark_wealth.csv")

    print("Returns data saved.")
    print(f"Returns shape: {returns.shape}")
    print(f"Asset returns shape: {asset_returns.shape}")
    print(f"Benchmark returns length: {benchmark_returns.shape[0]}")
    print("Benchmark wealth tail:")
    print(benchmark_wealth.tail())


if __name__ == "__main__":
    main()