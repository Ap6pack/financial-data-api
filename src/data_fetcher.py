import yfinance as yf
import requests
from cachetools import cached, TTLCache
from config import ALPHA_VANTAGE_KEY, FMP_KEY, QUANDL_KEY

# Cache results for 5 minutes to optimize API calls
cache = TTLCache(maxsize=100, ttl=300)

@cached(cache)
def get_stock_history(ticker, period="1mo"):
    stock = yf.Ticker(ticker)
    return stock.history(period=period).to_dict()

@cached(cache)
def get_technical_indicators(ticker, indicator="SMA"):
    url = f"https://www.alphavantage.co/query?function={indicator}&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}"
    response = requests.get(url)
    return response.json()

@cached(cache)
def get_fundamentals(ticker):
    url = f"https://financialmodelingprep.com/api/v3/ratios/{ticker}?apikey={FMP_KEY}"
    response = requests.get(url)
    return response.json()

@cached(cache)
def get_macro_data(dataset="FRED/GDP"):
    url = f"https://data.nasdaq.com/api/v3/datasets/{dataset}.json?api_key={QUANDL_KEY}"
    response = requests.get(url)
    return response.json()
