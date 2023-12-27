import yfinance as yf
import json

def main():
    print("Welcome to Stock Report v1.0.0 by Joshua Walter\n\n")
    watchlist = input("Please Enter The List Of Stocks You Want A Report On (tickers seperated by spaces):\n").split()
    #look for going through each ticker (run many different functions to pull data and compile report)
    for x in watchlist:
        try:
            #remember to see if there is any more financial indicators you need
            stock = yf.Ticker(x).info
            currentPrice = stock["currentPrice"]
            lastClose = stock["regularMarketPreviousClose"]
            dollarChange = currentPrice-lastClose
            percentChange = round((((currentPrice - lastClose)/lastClose) * 100), 2)
            priceToBook = stock["priceToBook"]
            trailingPriceToEarnings = stock["trailingPE"]
            forwardPriceToEarnings = stock["forwardPE"]
            fiftyDayMA = stock["fiftyDayAverage"]
            twoHundredDayMA = stock["twoHundredDayAverage"]
            dividendYield = stock["dividendYield"] * 100
            recommendationMean = stock["recommendationMean"]
            recommendationKey = stock["recommendationKey"]
            print("-"*20)
            print("Ticker: " + x + "\n")
            print("Current Price: " + str(currentPrice) + "\n\n")
            print("Last Close: " + str(lastClose) + "\n\n")
            print("Dollar Change: " + str(dollarChange) + "\n\n")
            print("Percent Change: " + str(percentChange) + "%\n\n")
            print("Price To Book: " + str(priceToBook) + "\n\n")
            print("Trailing Price To Earnings: " + str(trailingPriceToEarnings) + "\n\n")
            print("Forward Price To Earnings: " + str(forwardPriceToEarnings) + "\n\n")
            print("50 Day MA: " + str(fiftyDayMA) + "\n\n")
            print("200 Day MA: " + str(twoHundredDayMA) + "\n\n")
            print("Dividend Yield: " + str(dividendYield) + "%\n\n")
            print("Recommendations Average (1-5): \n" + str(recommendationMean) + "\n\n")
            print("Recommendations Key: \n" + recommendationKey + "\n\n")
            print("-"*20)
        except:
            print("Error: Possible incorrect ticker or code error") 
        

main()