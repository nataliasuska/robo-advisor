# this is the "app/robo_advisor.py" file
import os
import csv
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
from pandas import DataFrame

load_dotenv()
now = datetime.now()

digit = False
        
def to_usd(my_price):
    return f"${my_price:,.2f}"

while True:
    symbol = input("Please input a stock or cryptocurency ticker symbol between 1-5 characters long: ")
    try:
        float(symbol)
        print("Oops, your symbol might includes a number(s). Please try again!")
        continue
    except ValueError:
        pass
    if len(symbol)<1 or len(symbol)>5:
        print("Oops, we need a stock between 1 to 5 characters. Please try again!")
        continue
    for s in symbol:
        if s.isdigit():
            digit = True
            print("Oops, it looks like you used a number(s). Please try again!")
            continue
        elif digit == False:
            pass
    else:
        break

apikey = os.environ.get("ALPHAVANTAGE_API_KEY")

#this section is from https://colab.research.google.com/drive/1EH3xNXPrO4dniIW12X9ATDz1lMyMBREb?usp=sharing
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={apikey}"
response = requests.get(url)
parsed_response = json.loads(response.text)

error_message = "Error Message"
if error_message in parsed_response:
    print("An error has caused Nat-Bot's Stock Advisor to force quit, likely from unsupported characters or numbers. Please try again.")
    exit()
else:
    pass

records = []
for date, daily_data in parsed_response["Time Series (Daily)"].items():
    record = {
        "date": date,
        "open": float(daily_data["1. open"]),
        "high": float(daily_data["2. high"]),
        "low": float(daily_data["3. low"]),
        "close": float(daily_data["4. close"]),
        "volume": int(daily_data["5. volume"]),
    }
    records.append(record)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys())
latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]

# this is section, minus the variables, is from https://github.com/prof-rossetti/intro-to-python/blob/master/projects/robo-advisor/README.md
print("-------------------------")
print("SELECTED SYMBOL: ", symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ",now.strftime('%I:%M %p'), "on", now.strftime('%b %d, %Y'))
print("-------------------------")
print("LATEST DAY: ", last_refreshed)
print("LATEST CLOSE: ", to_usd(float(latest_close)))
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")