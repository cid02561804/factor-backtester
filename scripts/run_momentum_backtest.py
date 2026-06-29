from factor_backtester.analytics.returns import compute_simple_returns
from factor_backtester.backtest.benchmark import split_assets_and_benchmark
from factor_backtester.backtest.engine import backtest_from_weights
from factor_backtester.data.cleaning import load_and_clean_prices
from factor_backtester.data.universe import compute_eligibility_mask
from factor_backtester.factors.momentum import compute_momentum_signal
from factor_backtester.portfolio.construction import select_top_n
from factor_backtester.portfolio.rebalancing import get_monthly_rebalance_dates
from factor_backtester.portfolio.weighting import equal_weight_portfolio


def main() -> None:
    prices = load_and_clean_prices("data/processed/prices_clean.csv")
    returns = compute_simple_returns(prices)

    asset_returns, benchmark_returns = split_assets_and_benchmark(returns, benchmark_col="SPY")

    asset_prices = prices.drop(columns=["SPY"])
    eligibility = compute_eligibility_mask(asset_prices, min_history=252)

    momentum_signal = compute_momentum_signal(asset_prices, lookback=252, skip=21)

    rebalance_dates = get_monthly_rebalance_dates(asset_returns.index)

    monthly_signal = momentum_signal.loc[rebalance_dates]
    monthly_eligibility = eligibility.loc[rebalance_dates]

    selection = select_top_n(monthly_signal, monthly_eligibility, n=5)
    weights = equal_weight_portfolio(selection)

    portfolio_returns, portfolio_wealth = backtest_from_weights(asset_returns, weights)

    selection.astype(int).to_csv("data/processed/momentum_selection.csv")
    weights.to_csv("data/processed/momentum_weights.csv")
    portfolio_returns.to_frame(name="momentum_returns").to_csv("data/processed/momentum_returns.csv")
    portfolio_wealth.to_frame(name="momentum_wealth").to_csv("data/processed/momentum_wealth.csv")

    print("Momentum backtest complete.")
    print(f"Signal shape: {momentum_signal.shape}")
    print(f"Monthly selection shape: {selection.shape}")
    print("Portfolio wealth tail:")
    print(portfolio_wealth.tail())
    print("Benchmark wealth tail preview:")
    print((1 + benchmark_returns.fillna(0)).cumprod().tail())


if __name__ == "__main__":
    main()