import yfinance as yf
import matplotlib.pyplot as plt
import os

def determine_wealth(symbol, period):
    stock = yf.download(symbol, period=period)

    stock["MA10"] = stock["Close"].rolling(10).mean()  # Fast Signal
    stock["MA50"] = stock["Close"].rolling(50).mean()  # Slow Signal

    stock["Shares"] = [1 if stock.loc[ei, "MA10"] > stock.loc[ei, "MA50"] else 0 for ei in stock.index]

    stock["Close1"] = stock["Close"].shift(-1)
    stock["Profit"] = [stock.loc[ei,"Close1"] - stock.loc[ei, "Close"]
                       if stock.loc[ei, "Shares"] == 1
                       else 0 for ei in stock.index]

    stock["Wealth"] = stock["Profit"].cumsum()
    x = stock.tail(-49)
    stock["Buy-Hold"] = x["Close1"] - x.loc[x.index[0], "Close"]

    stock = stock.tail(-48)
    stock.to_csv(f"{symbol}/{symbol} for {period}.csv")

    return stock

def ma_graph(symbol, stock, period):
    plt.cla()
    stock["Close"].plot()
    stock["MA10"].plot()
    stock["MA50"].plot()
    plt.legend()
    plt.title(f"Moving Averages for {symbol}")
    plt.savefig(f"{symbol}/Moving Averages for {symbol} in {period}")

def wealth_graph(symbol, stock, period):
    plt.cla()
    stock["Wealth"].plot()
    stock["Buy-Hold"].plot()
    plt.legend()
    plt.title(f"Accumulated Wealth For {symbol} Using This Strategy")
    plt.savefig(f"{symbol}/Wealth Graph for {symbol} over {period}")

def daily_changes(symbol, stock, period):
    plt.cla()
    stock["Profit"].plot()
    plt.axhline(y=0, color="red")
    plt.ylabel("USD")
    plt.legend()
    plt.title(f"Daily Profit For {symbol} Using This Strategy")
    plt.savefig(f"{symbol}/Daily Profit for {symbol} over {period}")

def get_results(symbol, period):
    info = determine_wealth(symbol, period)
    ma_graph(symbol, info, period)
    wealth_graph(symbol, info, period)
    daily_changes(symbol, info, period)

    print("Total money you spent is $", info.loc[info.index[0], "Close"].round())
    print("Total money you earned following this strategy is $", info.loc[info.index[-2], "Wealth"].round())
    print("Total money you would have earned with a Buy and Hold Strategy is $",
          (info.loc[info.index[-2], "Buy-Hold"]).round(2))

def get_user_input():
    symbol = input("Choose a Stock Symbol (eg. AAPL): ")
    period = input("Pick a time period: ")
    options = ["3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]

    while period in options == False:
        period = input(f"Invalid Period, Please Choose Out Of The Available Options\n{options}\nPick a time period:")

    symbol = symbol.upper()
    try:
        os.mkdir(f"{symbol}")
        get_results(symbol,period)
    except:
        get_results(symbol,period)

get_user_input()