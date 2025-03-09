from fastapi import FastAPI, HTTPException
from data_fetcher import get_stock_history, get_fundamentals, get_technical_indicators, get_macro_data

app = FastAPI(title="Financial Data API")

@app.get("/")
def home():
    return {"message": "Welcome to the Financial Data API!"}

@app.get("/stock/{ticker}")
def get_stock_data(ticker: str):
    try:
        return {
            "history": get_stock_history(ticker),
            "fundamentals": get_fundamentals(ticker),
            "technical": get_technical_indicators(ticker)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/macro")
def get_macro_data_endpoint():
    try:
        return get_macro_data()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))