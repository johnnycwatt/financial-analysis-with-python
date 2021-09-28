The Simple Moving Average is a good indicator used by traders to determine market trends.

In one of the examples provided, the program determines the 50 day SMA and the 200 day SMA of a stock.
In this case, the 50 Day SMA will be known as the Fast Signal, while the 200 day SMA will be the slow signal of the stock.

Many traders believe that if the Fast Signal is higher than the Slow Signal (The 50 day SMA is higher than the 200 day SMA), 
then it is a good indicator that the stock price will go up. Alternatively if the Slow Signal is higher than the Fast signal,
it is a good indicator that the stock price will go down.

The program collects the stock price data from Yahoo Finance via the yfinance python module. 
The data is stored in a dataframe and then the program appends the dataframe provided by yfinance to include 
the Next Days Closing Price, The Daily Price Change and the Daily Returns. 
Finally the program determines the Moving Day Averages for the days set. 

The program saves this data into a CSV File, and also generates a graph visualising the two Moving Day Averages and the Stocks Closing Price
over a selected period of time. I have uploaded examples for stocks Amazon, Apple, Google and Facebook.

This is not intended to serve as Investment Advice, and is meant for educational purposes of how to determine and display the SMA of a Stock using Python.
