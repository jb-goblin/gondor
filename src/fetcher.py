import requests
import pandas as pd
from config import POSITIONS_URL, GAMMA_URL


def enrich_with_metadata(positions: pd.DataFrame) -> pd.DataFrame:
    """
    Placeholder function: TODO explore metadata available for contracts
    """

    gamma_resp = requests.get(GAMMA_URL)
    gamma_resp.raise_for_status()
    metadata_data = gamma_resp.json()

    metadata = pd.json_normalize(metadata_data)

    positions = positions.merge(
        metadata,
        how="left",
        left_on=["slug"],
        right_on=["slug"],
    )

    return positions


def positions_fetcher(user: str) -> pd.DataFrame:
    positions_params = {"user": user, "resolved": "false"}

    resp = requests.get(POSITIONS_URL, params=positions_params)
    resp.raise_for_status()
    positions_data = resp.json()
    print(f"fetched positions data with resp {resp}")
    positions = pd.DataFrame(positions_data)
    # positions_df.to_csv("C:\Projects\gondor\positions.csv", index=False)
    return positions


def fetch_polymarket_positions(user: str) -> pd.DataFrame:

    positions = positions_fetcher(user=user)
    # positions = enrich_with_metadata(positions=positions)
    return positions
