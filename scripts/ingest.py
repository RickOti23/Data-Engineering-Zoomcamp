import pandas as pd
import numpy as np
import yfinance as yf
from dotenv import load_dotenv
from datetime import datetime as dt, timedelta
from time import sleep
import os

load_dotenv()

start = "2020-01-01"
end = (dt.today() - timedelta(days=1)).strftime("%Y-%m-%d")

tickers = ['AAPL','MSFT','AMZN','GOOGL','GOOG','META','NVDA','TSLA',
           'JPM', 'BAC','WMT','DIS','XOM',"CVX",'NFLX']

def extract_data():
    dfs = []
    for ticker in tickers:
        obj = yf.Ticker(ticker)
        df = obj.history(start=start, end=end, interval="1d")
        df["ticker"] = ticker
        dfs.append(df)
        sleep(1)
    full_df = pd.concat(dfs)
    return full_df

def saving_locally(df):
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/stock_data.csv")
    print("Data saved to data/stock_data.csv")

if __name__ == "__main__":
    full_df = extract_data()
    saving_locally(full_df)