# this is the "app/robo_advisor.py" file
import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
now = datetime.now()



while True:
    symbol = input("Please input a stock or cryptocurency ticker symbol: ")
    try:
        float(symbol)
        print("Oops, your symbol might includes a number(s). Please try again!")
        continue
    except ValueError:
        pass

    if len(symbol)<1 or len(symbol)>5:
        print("Oops, we need a stock between 1 to 5 characters. Please try again!")
        continue
    elif symbol.lower() in symbol:
        print("Oops, looks like a duplicate. Please try again!")
        continue
    else:
        symbol.append(symbol.lower())
    


for stock in symbol:
    apikey = os.environ.get("ALPHAVANTAGE_API_KEY")

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&ap"
response = requests.get(url)
readable=json.loads(response.text)

last_refreshed = readable["Meta Data"]["Last Refreshed"]



# this is mostly from https://github.com/prof-rossetti/intro-to-python/blob/master/projects/robo-advisor/README.md
print("-------------------------")
print("SELECTED SYMBOL: ", stock)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ",now.strftime('%I:%M %p'), "on", now.strftime('%b %d, %Y'))
print("-------------------------")
print("LATEST DAY: ", last_refreshed)
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")