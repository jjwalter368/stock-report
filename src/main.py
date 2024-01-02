import yfinance as yf
from tabulate import tabulate
import pandas as pd
import json

def main():
    print("Welcome to Stock Report v1.0.0 by Joshua Walter\n\n")
    watchlist = input("Please Enter The List Of Stocks You Want A Report On (tickers seperated by spaces):\n").split()
    #look for going through each ticker (run many different functions to pull data and compile report)
    dict = {
        'Ticker': [],
        'Current Price': [],
        'Last Close': [],
        'Dollar Change': [],
        'Percent Change': [],
        'P/B': [],
        'Trailing P/E': [],
        'Forward P/E': [],
        '50 MA': [],
        '200 MA': [],
    }
    for x in watchlist:
        try:
            #remember to see if there is any more financial indicators you need
            stock = yf.Ticker(x).info
            dict["Ticker"].append(x)
            try:
                currentPrice = stock["currentPrice"]
                dict["Current Price"].append(str(currentPrice))
            except:
                dict["Current Price"].append("N/A")
            try:
                lastClose = stock["regularMarketPreviousClose"]
                dict["Last Close"].append(str(lastClose))
            except:
                dict["Last Close"].append("N/A")
            try:
                dollarChange = round(currentPrice-lastClose, 2)
                dict["Dollar Change"].append("$" + str(dollarChange))
            except:
                dict["Dollar Change"].append("N/A")
            try:
                percentChange = round((((currentPrice - lastClose)/lastClose) * 100), 2)
                dict["Percent Change"].append(str(percentChange) + "%")
            except:
                dict["Percent Change"].append("N/A")
            try:
                priceToBook = stock["priceToBook"]
                dict["P/B"].append(str(priceToBook))
            except:
                dict["P/B"].append("N/A")
            try:
                trailingPriceToEarnings = stock["trailingPE"]
                dict["Trailing P/E"].append(str(trailingPriceToEarnings))
            except:
                dict["Trailing P/E"].append("N/A")
            try:
                forwardPriceToEarnings = stock["forwardPE"]
                dict["Forward P/E"].append(str(forwardPriceToEarnings))
            except:
                dict["Forward P/E"].append("N/A")
            try:
                fiftyDayMA = stock["fiftyDayAverage"]
                dict["50 MA"].append(str(fiftyDayMA))
            except:
                dict["50 MA"].append("N/A")
            try:
                twoHundredDayMA = stock["twoHundredDayAverage"]
                dict["200 MA"].append(str(twoHundredDayMA))
            except:
                dict["200 MA"].append("N/A")

            #legacy version for just printing the information out into console
            #print("-"*20)
            #print("Ticker: " + x + "\n")
            #print("Current Price: " + str(currentPrice) + "\n\n")
            #print("Last Close: " + str(lastClose) + "\n\n")
            #print("Dollar Change: " + str(dollarChange) + "\n\n")
            #print("Percent Change: " + str(percentChange) + "%\n\n")
            #print("Price To Book: " + str(priceToBook) + "\n\n")
            #print("Trailing Price To Earnings: " + str(trailingPriceToEarnings) + "\n\n")
            #print("Forward Price To Earnings: " + str(forwardPriceToEarnings) + "\n\n")
            #print("50 Day MA: " + str(fiftyDayMA) + "\n\n")
            #print("200 Day MA: " + str(twoHundredDayMA) + "\n\n")
            #print("Dividend Yield: " + str(dividendYield) + "%\n\n")
            #print("Recommendations Average (1-5): \n" + str(recommendationMean) + "\n\n")
            #print("Recommendations Key: \n" + recommendationKey + "\n\n")
            #print("-"*20)
        except:
            print("Error: Possible incorrect ticker or code error") 
            print(x)
    try:
        df = pd.DataFrame(dict)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    except:
        jsondict = json.dumps(dict, indent=4)
        print(jsondict)

main()