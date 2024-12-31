import time
import yfinance as yf

# Gets data from api.
def get_data(symbol):
    stock = yf.Ticker(symbol)

    # Gets last data available.
    current = stock.history(period="1d")

    return current['Close'][-1], current.index[-1].strftime("%Y-%m-%d"), current.index[-1].strftime("%H:%M:%S")

# Gets historical data from api.
def get_historical(symbol, period="5y"):
    stock = yf.Ticker(symbol)
    historical = stock.history(period="5y")

    return historical