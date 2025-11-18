import numpy as np
import pandas as pd


def calculate_loan_expiry(portfolio: pd.DataFrame) -> int:

    min_expiry_proximity = portfolio["expiry_proximity"].min()

    return min_expiry_proximity
