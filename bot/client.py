from dotenv import load_dotenv
from binance.client import Client
import os

load_dotenv()


def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError(
            "API credentials not found. Please configure the .env file."
        )

    client = Client(
        api_key=api_key,
        api_secret=api_secret,
        testnet=True
    )