import matplotlib.pyplot as plt
import yfinance as yf

"""Getting the Moving Average for 200 days and 50 days"""

def moving_average(symbol, fast, slow, period):
    stock = yf.download(symbol, period=period)
    stock["PriceX"] = stock["Close"].shift(-1) #PriceX is the closing price of the next day
    stock["PriceDiff"] = stock["PriceX"] - stock["Close"] #Price Diff is the difference between Tomorrow and Today

    stock["Return"] = stock["PriceDiff"]/stock["Close"]
    stock["Direction"] = [1 if stock.loc[ei, "PriceDiff"] > 0 else -1 for ei in stock.index]

    stock[f"MA{fast}"] = stock["Close"].rolling(fast).mean() #Fast Signal
    stock[f"MA{slow}"] = stock["Close"].rolling(slow).mean() #Slow Signal

    stock = stock.tail(-slow)
    stock.to_csv(f"{symbol}_{fast}_and_{slow}_day_moving_averages.csv")
    generate_graph(symbol, fast, slow, stock)

def generate_graph(symbol, fast, slow, stock):
    stock["Close"].plot()
    stock[f"MA{fast}"].plot()
    stock[f"MA{slow}"].plot()
    plt.title(f"{fast} DAYS AND {slow} DAYS MOVING AVERAGES FOR {symbol}")
    plt.legend()
    plt.savefig(f"{symbol}_{fast}_and_{slow}_day_moving_averages")
    plt.cla()

moving_average("AMZN", 20, 100, "1y")
moving_average("GOOG", 50, 200, "5y")
moving_average("AAPL", 20, 100, "1y")
moving_average("FB", 50, 200, "5y")