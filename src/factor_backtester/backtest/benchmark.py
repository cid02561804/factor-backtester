import pandas as pd


def split_assets_and_benchmark(
    returns: pd.DataFrame,
    benchmark_col: str = "SPY",
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Split a returns DataFrame into asset returns and benchmark returns.
    """
    if benchmark_col not in returns.columns:
        raise ValueError(f"Benchmark column '{benchmark_col}' not found in returns DataFrame.")

    benchmark = returns[benchmark_col].copy()
    assets = returns.drop(columns=[benchmark_col]).copy()

    return assets, benchmark