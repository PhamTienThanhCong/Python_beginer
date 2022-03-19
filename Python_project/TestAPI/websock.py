import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

spot_client = Client(base_url="https://testnet.binance.vision")

data = []

data = spot_client.klines("BTCUSDT", "1m")
# logging.info(spot_client.klines("BTCUSDT", "1h", limit=1))

for i in range(0,(len(data))):
    print(data[i])