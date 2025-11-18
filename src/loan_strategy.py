"""
Build a draft system for the loan strategy
"""

import pandas as pd

from config import DOMER_WALLET
from fetcher import fetch_polymarket_positions
from calculate_ltv import calculate_ltv_haircut
from calculate_eligibility import calculate_eligibility
from calculate_loan_expiry import calculate_loan_expiry


def cleanup_portfolio(portfolio: pd.DataFrame) -> pd.DataFrame:

    return portfolio


def run_portfolio_strategy():

    portfolio = fetch_polymarket_positions(user=DOMER_WALLET)
    portfolio = calculate_ltv_haircut(portfolio=portfolio, k=1)

    portfolio = calculate_eligibility(portfolio=portfolio)

    whitelisted_portfolio = portfolio[portfolio["whitelist"] == True]
    loan_amount = (portfolio["max_ltv"] * portfolio["currentValue"]).sum()
    loan_expiry = calculate_loan_expiry(portfolio=whitelisted_portfolio)

    print(f"Loan amount: {loan_amount}")
    print(f"Loan expiry: {loan_expiry} days")

    return loan_amount, loan_expiry


run_portfolio_strategy()
