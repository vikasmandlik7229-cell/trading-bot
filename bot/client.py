from binance.client import Client
from dotenv import load_dotenv
import os
import time

load_dotenv()


def get_client():
    client = Client(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET")
    )

    
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    
    server_time = client.futures_time()['serverTime']
    system_time = int(time.time() * 1000)

    client.timestamp_offset = server_time - system_time

    return client