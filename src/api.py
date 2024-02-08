from flask import Flask
import yfinance as yf
from tabulate import tabulate
import pandas as pd
import json
import os
import time
from main import *
class Stock:
    def __init__(self):
        self.Ticker = None
        self.Current_Price = None
        self.Last_Close = None
        self.Dollar_Change = None
        self.Percent_Change = None
        self.PB = None
        self.Trailing_PE = None
        self.Forward_PE = None
        self.MA50 = None
        self.MA200 = None
    def export(self):
        exportDict = {
            "Ticker": self.Ticker,
            "Current Price": self.Current_Price,
            "Last Close": self.Last_Close,
            "Dollar Change": self.Dollar_Change,
            "Percent_Change": self.Percent_Change,
            "P/B": self.PB,
            "Trailing P/E": self.Trailing_PE,
            "Forward_PE": self.Forward_PE,
            "50 MA": self.MA50,
            "200 MA": self.MA200,
        }
        return exportDict
app = Flask(__name__)
@app.route('/<input>')
def apiPlain(input):
    watchlist = input.split(",")
    stockList = []
    #until exited, initialize a blank-slate dictionary, then assign the variables pulled from yahoo finance, then create the data frame...
    #clear the screen, add the vertical margins, then print the table while adding the horizontal margins, with an exception clause ...
    #Then wait 5 seconds and clear the screen and print the verticle margins again
    for x in watchlist:
        exec(f"{x} = Stock()")
        exec(f"{x}.")
        stock = yf.Ticker(x).info
        exec(f"{x}.Ticker = stock['{x}']")
        try:
            exec(f"{x}.Current_Price = str(stock['currentPrice'])")
        except:
            exec(f"{x}.Current_Price = 'N/A'")
        try:
            exec(f"{x}.Last_Close = str(stock['regularMarketPreviousClose'])")
        except:
            exec(f"{x}.Last_Close = 'N/A'")
        try:
            exec(f"{x}.Dollar_Change = round(stock[currentPrice]-stock[lastClose], 2)")
        except:
            exec(f"{x}.Dollar_Change = 'N/A'")
        try:
            exec(f"{x}.Percent_Change = round((((stock[currentPrice] - stock[lastClose])/stock[lastClose]) * 100), 2)")
        except:
            exec(f"{x}.Percent_Change = 'N/A'")
        try:
            exec(f"{x}.PB = str(stock['priceToBook'])")
        except:
            exec(f"{x}.PB = 'N/A'")
        try:
            exec(f"{x}.Trailing_PE = stock['trailingPE']")
        except:
            exec(f"{x}.Trailing_PE = 'N/A'")
        try:
            exec(f"{x}.Forward_PE = stock['forwardPE']")
        except:
            exec(f"{x}.Forward_PE = 'N/A'")
        try:
            exec(f"{x}.MA50 = stock['fiftyDayAverage']")
        except:
            exec(f"{x}.MA50 = 'N/A'")
        try:
            exec(f"{x}.MA200 = stock['twoHundredDayAverage']")
        except:
            exec(f"{x}.MA200 = 'N/A'")
        exec(f"stockList.append({x})")
    try:
        for x in stockList:
            y = {}
            y[f"{x}"] = x.export()
            return y
    except Exception as error:
        #Throws error and dumps the dict data for debugging purposes
        return error

app.run()