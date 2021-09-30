import yfinance as yf
import matplotlib.pyplot as plt


def get_info(symbol,period, investment):
    info = yf.download(symbol, period=period)

    shares = (investment/(info.loc[info.index[0], "Close"])).round(2) #How many shares we can buy with our investment
    info["Wealth"] = info["Close"]*shares

    if period == "1y":
        print(f"You would have owned {shares} shares if you had invested in {symbol} 1 Year ago")
    else:
        print(f"You would have owned {shares} shares if you had invested in {symbol} 5 Years ago")
    return info




def comparison(symbol1, symbol2, investment):
    i = get_info(symbol1, "1y", investment) #One Year Investment in Stock 1
    j = get_info(symbol2, "1y", investment) #One Year Investment in Stock 2
    x = get_info(symbol1, "5y", investment) #Five Year Investment in Stock 1
    y = get_info(symbol2, "5y", investment) #Five Year Investment in Stock 2

    investment1_1y = i.loc[i.index[-1], "Wealth"].round(2) #Todays Value Stock 1, 1 Year Period
    investment2_1y = j.loc[j.index[-1], "Wealth"].round(2) #Todays Value Stock 2, 5 Year Period

    investment1_5y = x.loc[x.index[-1], "Wealth"].round(2) #Todays Value Stock 1, 5 Year Period
    investment2_5y = y.loc[y.index[-1], "Wealth"].round(2) #Todays Value Stock 2, 5 Year Period

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10,10))

    ax1.plot(i["Wealth"])
    ax1.plot(j["Wealth"])
    ax1.set_title(f"One Year Investment of ${investment:,} in {symbol1} vs {symbol2}")
    ax2.set_title(f"Five Year Investment of ${investment:,} in {symbol1} vs {symbol2}")

    ax1.set_ylabel("Stock Price $USD")
    ax2.set_ylabel("Stock Price $USD")

    ax2.plot(x["Wealth"])
    ax2.plot(y["Wealth"])

    ax1.legend([f"{symbol1}: ${investment1_1y:,}", f"{symbol2}: ${investment2_1y:,}"])
    ax2.legend([f"{symbol1}: ${investment1_5y:,}", f"{symbol2}: ${investment2_5y:,}"])

    plt.tight_layout
    plt.savefig(f"{symbol1} and {symbol2} comparison")


    print(f"You're inital investment was: ${investment}")
    print(f"\nIf you had invested ${investment:,} in {symbol1} 1 year ago, "
          f"today your investment would be worth: ${investment1_1y:,}")
    print(f"\nIf you had invested ${investment:,} in {symbol2} 1 year ago, "
          f"today your investment would be worth: ${investment2_1y:,}")

    print(f"\nIf you had invested ${investment:,} in {symbol1} 5 years ago, "
          f"today your investment would be worth: ${investment1_5y:,}")
    print(f"\nIf you had invested ${investment:,} in {symbol2} 5 years ago, "
          f"today your investment would be worth: ${investment2_5y:,}")



def get_user_info():
    symbol1 = input("Choose a Stock(eg: AAPL): ").upper().strip()
    symbol2 = input("Choose a Stock(eg: GOOG: ").upper().strip()
    investment = input("How much money would you like to put in: ")

    try:
        investment = int(investment)
    except:
        print("Sorry. You did not choose a valid number")
        return

    comparison(symbol1, symbol2, investment)

get_user_info()

