from factor_backtester.analytics.metrics import compute_wealth_index
from factor_backtester.analytics.returns import compute_simple_returns
from factor_backtester.backtest.benchmark import split_assets_and_benchmark
from factor_backtester.backtest.costs import (
    apply_transaction_costs,
    compute_turnover,
    transaction_costs_from_turnover,
)
from factor_backtester.backtest.engine import backtest_from_weights
from factor_backtester.data.cleaning import load_and_clean_prices
from factor_backtester.data.universe import compute_eligibility_mask
from factor_backtester.factors.momentum import compute_momentum_signal
from factor_backtester.portfolio.construction import select_top_n
from factor_backtester.portfolio.rebalancing import get_monthly_rebalance_dates
from factor_backtester.portfolio.weighting import equal_weight_portfolio
from factor_backtester.utils.config import load_yaml_config


def main() -> None:
    base_config = load_yaml_config("configs/base.yaml")
    strategy_config = load_yaml_config("configs/momentum.yaml")

    benchmark = base_config["data"]["benchmark"]
    min_history = base_config["portfolio"]["min_history"]
    n_assets = base_config["portfolio"]["n_assets"]
    cost_bps = base_config["costs"]["transaction_cost_bps"]

    lookback = strategy_config["strategy"]["lookback"]
    skip = strategy_config["strategy"]["skip"]

    prices = load_and_clean_prices("data/processed/prices_clean.csv")
    returns = compute_simple_returns(prices)

    asset_returns, _ = split_assets_and_benchmark(returns, benchmark_col=benchmark)
    asset_prices = prices.drop(columns=[benchmark])
    eligibility = compute_eligibility_mask(asset_prices, min_history=min_history)

    signal = compute_momentum_signal(asset_prices, lookback=lookback, skip=skip)
    rebalance_dates = get_monthly_rebalance_dates(asset_returns.index)

    monthly_signal = signal.loc[rebalance_dates]
    monthly_eligibility = eligibility.loc[rebalance_dates]

    selection = select_top_n(monthly_signal, monthly_eligibility, n=n_assets)
    weights = equal_weight_portfolio(selection)

    gross_returns, gross_wealth = backtest_from_weights(asset_returns, weights)

    turnover = compute_turnover(weights)
    costs = transaction_costs_from_turnover(turnover, cost_bps=cost_bps)
    net_returns = apply_transaction_costs(gross_returns, costs)
    net_wealth = compute_wealth_index(net_returns)

    turnover.to_frame(name="turnover").to_csv("data/processed/momentum_turnover.csv")
    costs.to_frame(name="transaction_cost").to_csv("data/processed/momentum_costs.csv")
    gross_returns.to_frame(name="momentum_gross_returns").to_csv("data/processed/momentum_gross_returns.csv")
    net_returns.to_frame(name="momentum_net_returns").to_csv("data/processed/momentum_net_returns.csv")
    gross_wealth.to_frame(name="momentum_gross_wealth").to_csv("data/processed/momentum_gross_wealth.csv")
    net_wealth.to_frame(name="momentum_net_wealth").to_csv("data/processed/momentum_net_wealth.csv")

    print("Momentum backtest with transaction costs complete.")
    print("Turnover tail:")
    print(turnover.tail())
    print("Gross wealth tail:")
    print(gross_wealth.tail())
    print("Net wealth tail:")
    print(net_wealth.tail())


if __name__ == "__main__":
    main()