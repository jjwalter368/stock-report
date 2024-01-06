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

def displayTable(df):
    #clears screen and prints vertical margins
    clsOrient()
    #print the width margins and the table
    for x in tabulate(df, headers = 'keys', tablefmt = 'psql', stralign='center').split("\n"):
                print(widthMargins*" " + x)
    

def pullInfo(ticker, dictionary):
        try:
            #develop a function for pulling the info for a stock (intakes the ticker and the dictionary so it can update it)
            stock = yf.Ticker(ticker).info
            dict["Ticker"].append(ticker)
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
        except Exception as error:
            print(error + "\n") 
            print(ticker)

def main():
    global dict
    #until exited, initialize a blank-slate dictionary, then assign the variables pulled from yahoo finance, then create the data frame...
    #clear the screen, add the vertical margins, then print the table while adding the horizontal margins, with an exception clause ...
    #Then wait 5 seconds and clear the screen and print the verticle margins again
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
            pullInfo(x, dict)
        try:
            df = pd.DataFrame(dict)
            displayTable(df)
        except Exception as error:
            #Throws error and dumps the dict data for debugging purposes
            jsondict = json.dumps(dict, indent=4)
            print(jsondict)
            print(error)
        #Waits 5 seconds then clears the terminal. measures the size of the window, and adds the verticle margin
        time.sleep(5)

main()