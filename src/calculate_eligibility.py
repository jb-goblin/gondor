import random
import pandas as pd
import numpy as np
from datetime import datetime, date


def fetch_liquidity_data(slug: str, transaction_span: float, size: float):
    """
    This is a placeholder function. The idea is to fetch order book history to estimate a contract's liquidity.

    :param transaction_span: number of hours over which to look at the transaction volume
    (param size here is just to initialise the random values)
    """

    market_size = random.uniform(1, 100) * size
    volume = random.uniform(0, 50) * size

    return market_size, volume


def calculate_eligibility(portfolio: pd.DataFrame) -> pd.DataFrame:

    liquidity_data = portfolio["size"].apply(
        lambda size: fetch_liquidity_data("placeholder", 24, size)
    )
    portfolio["market_size"] = liquidity_data.apply(lambda x: x[0])
    portfolio["volume"] = liquidity_data.apply(lambda x: x[1])

    today = date.today()
    portfolio["expiry_proximity"] = portfolio["endDate"].apply(
        lambda end_date: (datetime.strptime(end_date, "%Y-%m-%d").date() - today).days
    )

    # Checks the position size is inferior to x% of the market,
    # that the size compared to last day's volume is inferior to y% to avoid slippage,
    # and check there are more than 3 days left until expiry (this is very crude, exploring theta calculations for
    # prediction markets can be interesting)
    portfolio["whitelist"] = (
        (portfolio["size"] / portfolio["market_size"] < 0.05)
        & (portfolio["size"] / portfolio["volume"] < 0.1)
        & (portfolio["expiry_proximity"] > 3)
    )

    return portfolio
