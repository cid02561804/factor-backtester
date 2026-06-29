import numpy as np
import pandas as pd

from factor_backtester.factors.momentum import compute_momentum_signal


def test_compute_momentum_signal_basic_case():
    prices = pd.DataFrame(
        {
            "A": [100, 110, 121, 133.1],
        },
        index=pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"]),
    )

    signal = compute_momentum_signal(prices, lookback=2, skip=1)

    expected_value = 110 / 100 - 1
    assert np.isclose(signal.loc["2024-01-03", "A"], expected_value)