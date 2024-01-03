import yfinance as yf
from tabulate import tabulate
import pandas as pd
import json
import os
import time

print("Welcome to Stock Report v1.0.0 by Joshua Walter\n\n")
watchlist = input("Please Enter The List Of Stocks You Want A Report On (tickers seperated by spaces):\n").split()

def windowMeasure():
    global height, heightMargins, width, widthMargins
    height = os.get_terminal_size().lines
    heightMargins = int(round((height-len(watchlist)-4)/2,0))
    width = os.get_terminal_size().columns
    widthMargins = int(round(((width-151)/2),0))
    if widthMargins < 0:
        widthMargins = 0

def clsOrient():
    windowMeasure()
    #need to learnd about the one line functions and control like this has, will make simpler for now
    #os.system('cls' if os.name=='nt' else 'clear')
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    #print("\n" * int((round(os.get_terminal_size().lines)/2, 0)))
    print("\n" * heightMargins)

def main():
    #look for going through each ticker (run many different functions to pull data and compile report)
    while True:
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
            clsOrient()
            #add a width margin by splitting the tabulate string by '\n' and adding half the width of the screen minus the width of the box
            #151 chars
            for x in tabulate(df, headers = 'keys', tablefmt = 'psql', stralign='center').split("\n"):
                print(widthMargins*" " + x)
        except Exception as error:
            jsondict = json.dumps(dict, indent=4)
            print(jsondict)
            print(error)
        time.sleep(10)
        clsOrient()

main()