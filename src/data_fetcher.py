from cache import get_cached_data, set_cached_data
import yfinance as yf
import requests
from config import ALPHA_VANTAGE_KEY, FMP_KEY, QUANDL_KEY

def get_stock_history(ticker, period="1mo"):
    """Fetch stock history with caching."""
    cache_key = f"stock_history_{ticker}_{period}"
    cached_result = get_cached_data(cache_key)
    
    if cached_result:
        return cached_result

    stock = yf.Ticker(ticker)
    data = stock.history(period=period).to_dict()
    
    set_cached_data(cache_key, data)
    return data

def get_technical_indicators(ticker, indicator="SMA"):
    """Fetch technical indicators with caching."""
    cache_key = f"technical_{ticker}_{indicator}"
    cached_result = get_cached_data(cache_key)

    if cached_result:
        return cached_result

    url = f"https://www.alphavantage.co/query?function={indicator}&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}"
    response = requests.get(url)
    data = response.json()
    
    set_cached_data(cache_key, data)
    return data

def get_fundamentals(ticker):
    """Fetch fundamental data with caching."""
    cache_key = f"fundamentals_{ticker}"
    cached_result = get_cached_data(cache_key)

    if cached_result:
        return cached_result

    url = f"https://financialmodelingprep.com/api/v3/ratios/{ticker}?apikey={FMP_KEY}"
    response = requests.get(url)
    data = response.json()
    
    set_cached_data(cache_key, data)
    return data

def get_macro_data(dataset="FRED/GDP"):
    """Fetch macroeconomic data with caching."""
    cache_key = f"macro_{dataset}"
    cached_result = get_cached_data(cache_key)

    if cached_result:
        return cached_result

    url = f"https://data.nasdaq.com/api/v3/datasets/{dataset}.json?api_key={QUANDL_KEY}"
    response = requests.get(url)
    data = response.json()
    
    set_cached_data(cache_key, data)
    return data
