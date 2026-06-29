import numpy as np
import pandas as pd


TRADING_DAYS_PER_YEAR = 252


def annualized_return(returns: pd.Series) -> float:
    returns = returns.dropna()
    if returns.empty:
        return np.nan
    return returns.mean() * TRADING_DAYS_PER_YEAR


def annualized_volatility(returns: pd.Series) -> float:
    returns = returns.dropna()
    if returns.empty:
        return np.nan
    return returns.std(ddof=1) * np.sqrt(TRADING_DAYS_PER_YEAR)


def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    returns = returns.dropna()
    if returns.empty:
        return np.nan

    daily_rf = risk_free_rate / TRADING_DAYS_PER_YEAR
    excess_returns = returns - daily_rf

    vol = excess_returns.std(ddof=1)
    if vol == 0:
        return np.nan

    return excess_returns.mean() / vol * np.sqrt(TRADING_DAYS_PER_YEAR)


def sortino_ratio(returns: pd.Series, target_return: float = 0.0) -> float:
    returns = returns.dropna()
    if returns.empty:
        return np.nan

    downside = returns[returns < target_return]
    if downside.empty:
        return np.nan

    downside_deviation = np.sqrt(((downside - target_return) ** 2).mean())
    if downside_deviation == 0:
        return np.nan

    return (returns.mean() - target_return) / downside_deviation * np.sqrt(TRADING_DAYS_PER_YEAR)


def compute_wealth_index(returns: pd.Series, initial_value: float = 1.0) -> pd.Series:
    returns = returns.fillna(0)
    return initial_value * (1 + returns).cumprod()


def cagr(returns: pd.Series) -> float:
    returns = returns.dropna()
    if returns.empty:
        return np.nan

    wealth = compute_wealth_index(returns)
    total_years = len(returns) / TRADING_DAYS_PER_YEAR
    if total_years == 0:
        return np.nan

    return (wealth.iloc[-1] / wealth.iloc[0]) ** (1 / total_years) - 1


def drawdown_series(returns: pd.Series) -> pd.Series:
    wealth = compute_wealth_index(returns)
    running_max = wealth.cummax()
    drawdowns = wealth / running_max - 1
    return drawdowns


def max_drawdown(returns: pd.Series) -> float:
    drawdowns = drawdown_series(returns)
    return drawdowns.min()


def performance_summary(returns: pd.Series, name: str = "strategy") -> pd.Series:
    return pd.Series(
        {
            "name": name,
            "annualized_return": annualized_return(returns),
            "cagr": cagr(returns),
            "annualized_volatility": annualized_volatility(returns),
            "sharpe_ratio": sharpe_ratio(returns),
            "sortino_ratio": sortino_ratio(returns),
            "max_drawdown": max_drawdown(returns),
        }
    )