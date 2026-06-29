from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def save_figure(fig: plt.Figure, save_path: str | None = None) -> None:
    if save_path is not None:
        path = Path(save_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=300, bbox_inches="tight")


def plot_cumulative_wealth(
    wealth_df: pd.DataFrame,
    title: str = "Cumulative Wealth",
    save_path: str | None = None,
) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))
    wealth_df.plot(ax=ax, linewidth=2)
    ax.set_title(title)
    ax.set_ylabel("Wealth Index")
    ax.set_xlabel("Date")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    save_figure(fig, save_path)
    plt.close(fig)


def plot_drawdowns(
    drawdown_df: pd.DataFrame,
    title: str = "Drawdowns",
    save_path: str | None = None,
) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))
    drawdown_df.plot(ax=ax, linewidth=2)
    ax.set_title(title)
    ax.set_ylabel("Drawdown")
    ax.set_xlabel("Date")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    save_figure(fig, save_path)
    plt.close(fig)


def plot_annual_returns(
    returns_df: pd.DataFrame,
    title: str = "Annual Returns",
    save_path: str | None = None,
) -> None:
    annual_returns = (1 + returns_df).groupby(returns_df.index.year).prod() - 1

    fig, ax = plt.subplots(figsize=(10, 6))
    annual_returns.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_ylabel("Annual Return")
    ax.set_xlabel("Year")
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    save_figure(fig, save_path)
    plt.close(fig)