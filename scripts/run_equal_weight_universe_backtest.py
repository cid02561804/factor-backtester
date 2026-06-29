from factor_backtester.backtest.engine import backtest_from_weights
from factor_backtester.data.cleaning import load_and_clean_prices
from factor_backtester.data.universe import compute_eligibility_mask
from factor_backtester.analytics.returns import compute_simple_returns
from factor_backtester.backtest.benchmark import split_assets_and_benchmark
from factor_backtester.portfolio.weighting import equal_weight_portfolio
from factor_backtester.portfolio.rebalancing import get_monthly_rebalance_dates


def main() -> None:
    prices = load_and_clean_prices("data/processed/prices_clean.csv")
    returns = compute_simple_returns(prices)

    asset_returns, benchmark_returns = split_assets_and_benchmark(returns, benchmark_col="SPY")

    eligibility = compute_eligibility_mask(prices.drop(columns=["SPY"]), min_history=252)

    rebalance_dates = get_monthly_rebalance_dates(asset_returns.index)
    selection = eligibility.loc[rebalance_dates].astype(bool)
    weights = equal_weight_portfolio(selection)

    portfolio_returns, portfolio_wealth = backtest_from_weights(asset_returns, weights)

    print("Backtest complete.")
    print("Portfolio return series head:")
    print(portfolio_returns.head())
    print("Portfolio wealth tail:")
    print(portfolio_wealth.tail())
    print("Benchmark return series head:")
    print(benchmark_returns.head())


if __name__ == "__main__":
    main()