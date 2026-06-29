# Methodology Notes

## Universe
The strategy universe consists of a small liquid large-cap US equity set used as a prototype research universe, with SPY used as the benchmark.

## Data
Historical daily adjusted close data is downloaded using Yahoo Finance and stored in raw and processed forms.

## Eligibility
A stock becomes eligible only after accumulating at least 252 valid daily observations.

## Rebalancing
Portfolios are rebalanced monthly using the last available trading day of each month.

## Momentum
Momentum is computed using a trailing lookback window with a skip period to avoid short-term reversal contamination.

## Low Volatility
Low-volatility is computed as trailing rolling standard deviation of daily returns.

## Costs
Transaction costs are modeled as a fixed basis-point charge applied to turnover at rebalance dates.