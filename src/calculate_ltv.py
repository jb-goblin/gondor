import random
import pandas as pd
import numpy as np


def calculate_atr(slug: str, atr_span: int):
    """
    This is a placeholder function. The idea is to fetch historical prices for a contract to calculate volatility.

    :param atr_span: number of hours over which to calculate the Average True Range
    """

    atr = random.uniform(0.01, 0.7)

    return atr


def calculate_ltv_haircut(portfolio: pd.DataFrame, k: float) -> pd.DataFrame:
    """
    Approximate binary outcome probability with market price.
    This assumes the market prices contracts efficiently.

    Assume additional collateral can be called every day if the value of collateral portfolio goes down.
    Calculate LTV as outcome probability - 24 hours price volatility

    :param k: adjustment variable
    """

    portfolio["atr"] = portfolio["slug"].apply(lambda slug: calculate_atr(slug, 24))
    portfolio["max_ltv"] = np.maximum(portfolio["curPrice"] - (k * portfolio["atr"]), 0)
    return portfolio
