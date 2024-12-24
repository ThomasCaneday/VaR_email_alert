import alpaca_trade_api as tradeapi
from config import *

# Alpaca API Credentials
API_KEY = API_KEY
API_SECRET = SECRET_KEY
BASE_URL = BASE_URL

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)

def get_realtime_data(symbols):
    barset = api.get_bars(symbols, '1Day', limit=50).df  # Fetch past 50 days of data
    data = {symbol: barset[barset['symbol'] == symbol] for symbol in symbols}
    return data

# symbols = ['AAPL', 'MSFT', 'NVDA']
# data = get_realtime_data(symbols)
# print(data)