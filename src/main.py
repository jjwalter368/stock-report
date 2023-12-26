import yfinance as yf
import json

def main():
    print("Welcome to Stock Report v1.0.0 by Joshua Walter\n\n")
    watchlist = input("Please Enter The List Of Stocks You Want A Report On (tickers seperated by spaces):\n").split()
    #look for going through each ticker (run many different functions to pull data and compile report)
    for x in watchlist:
        try:
            stock = yf.Ticker(x).info
            currentPrice = stock["currentPrice"]
            lastClose = stock["regularMarketPreviousClose"]
            dollarChange = currentPrice-lastClose
            percentChange = round((((currentPrice - lastClose)/lastClose) * 100), 2)
            #make sure to add ratios, book values, 200 day average, etc. (financial indicators and stats that I use)
            #maybe try to pull some news or get a positive/negative news indicator??
            recommendationMean = stock["recommendationMean"]
            recommendationKey = stock["recommendationKey"]
            print("Ticker: " + x + "\n")
            print("Current Price: " + str(currentPrice) + "\n\n")
            print("Last Close: " + str(lastClose) + "\n\n")
            print("Dollar Change: " + str(dollarChange) + "\n\n")
            print("Percent Change: " + str(percentChange) + "\n\n")
            print("Recommendations Average (1-5): \n" + str(recommendationMean) + "\n\n")
            print("Recommendations Key: \n" + recommendationKey + "\n\n")
        except:
            print("Error: Possible incorrect ticker or code error") 
        

main()