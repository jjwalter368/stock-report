import os
from tabulate import tabulate
from main import watchlist

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
    #need to learn about the one line functions and control like this has, will make simpler for now
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