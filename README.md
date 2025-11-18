# Quant Analyst test assignment

## Test description

As an exercise, we consider lending against positions from the largest Polymarket account ([Domer's](https://polymarket.com/@ImJustKen)). "How much would you let him borrow and at what terms?".

1. Which of Domer’s markets are eligible for being used as collateral
2. How much collateral total per every eligible market Gondor would allow to be used, assuming there are no other borrowers apart from Domer
3. For Domer’s eligible bundle collateral, how much USDC he can borrow
4. What fixed APR Domer will be charged for this loan
5. When the loan expires

## Approach

These 5 points are interlinked to form a coherent system. I chose point 3 (LTV) as a starting point, as it implies coming up with a definition of a market's risk.

- Assume markets efficiently estimate the probability of outcomes; calculate LTV as contract price - volatility
- Calculate eligibility based on the position's relative size compared to this contract's trading volume and market size and based on time to maturity
- Loan expiry as the smallest maturity in the eligible portfolio (suggestions for better approaches below)
- I didn't explore point 2, how much collateral per eligible market should be accepted; I think the main factor here will be analysing historical correlation between contract types
- I didn't have time to draft a calculation for point 4. Do we want APR to vary depending on the portfolio, or simply bill a standardised very high APR (like Kraken does for margin trading)?

## Python analysis set-up

run `pip install -r requirements.txt`

## Notes

### Loan expiry

Possible strategies:

- call for more collateral to replace assets within the collateral bundle which approach expiry
- staggered loan pay back to maintain an acceptable LTV as assets within the collateral bundel approach expiry
- model a time weighted risk profile for the collateral bundle at creation, and have a unique loan expiry

### Capping exposure

How to balance the collateral portfolio? A strategy here can be to identify risk factors driving contract prices, categorise them, and quantify correlations if possible.
