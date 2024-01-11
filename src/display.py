import os
from tabulate import tabulate

def windowMeasure(watchlist):
    global height, heightMargins, width, widthMargins
    height = os.get_terminal_size().lines
    heightMargins = int(round((height-len(watchlist)-4)/2,0))
    width = os.get_terminal_size().columns
    widthMargins = int(round(((width-151)/2),0))
    if widthMargins < 0:
        widthMargins = 0

def clsOrient(watchlist):
    windowMeasure(watchlist)
    #need to learn about the one line functions and control like this has, will make simpler for now
    #os.system('cls' if os.name=='nt' else 'clear')
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    #print("\n" * int((round(os.get_terminal_size().lines)/2, 0)))
    print("\n" * heightMargins)

def displayTable(df, watchlist):
    #clears screen and prints vertical margins
    clsOrient(watchlist)
    #print the width margins and the table
    for x in tabulate(df, headers = 'keys', tablefmt = 'psql', stralign='center').split("\n"):
                print(widthMargins*" " + x)
def displayGraph():
     #placeholder
     #probably need pandas and need to add the pulling of the historical stock data in main.py
     return True

def dispayDynamic():
     #placeholder
     return True

def displayStatic():
     #placeholder
     #still need to decide if I need to 
     return True