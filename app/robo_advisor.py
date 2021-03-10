import os
import csv
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
import matplotlib.pyplot as plt


load_dotenv()
now = datetime.now()
digit = False
apikey = os.environ.get("ALPHAVANTAGE_API_KEY")
        
def to_usd(my_price):
    return f"${my_price:,.2f}"

#for users to input their ticker and respond to errors
while True:
    symbol = input("Please input a valid stock or cryptocurency ticker symbol between 1-5 characters long, without spaces or numbers: ")
    try:
        float(symbol)
        print("Oops, it looks like you only inputted a number(s). Please try again!")
        continue
    except ValueError:
        pass
    if len(symbol)<1 or len(symbol)>5:
        print("Oops, we need a stock between 1 to 5 characters. Please try again!")
        continue
    for s in symbol:
        if s.isdigit():
            digit = True
            print("Oops, it looks like you used a number(s) among your symbols. Please try again!")
            continue
        elif digit == False:
            pass
    else:
        break


#this section is from https://colab.research.google.com/drive/1EH3xNXPrO4dniIW12X9ATDz1lMyMBREb?usp=sharing
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={apikey}"
response = requests.get(url)
parsed_response = json.loads(response.text)

#for all other errors
error = "Error Message"
if error in parsed_response:
    print("An error has caused Nat-Bot's Stock Advisor to force quit, likely from unsupported characters, numbers, or an invalid ticker. Please try again.")
    exit()
else:
    pass


#variable setup
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys())
latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]

high = []
low = []
for date in dates:
    high_price = tsd[date]["2. high"]
    high.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low.append(float(low_price))
recent_high = max(high)
recent_low = min(low)


#recommendations
stonks = ['gme', 'GME', 'gME', 'gmE', 'gMe', 'GmE', 'GMe', 'Gme', 'amc', 'AMC', 'aMC', 'amC', 'aMc', 'Amc', 'AMc', 'AmC', 'bb', 'BB', 'bB', 'Bb']
if symbol in stonks:  #having some fun here with the reddit memes and stocks
    recommend = "DIAMOND HANDS!!!"
    reason = "Nat-Bot sees that you have chosen either gamestop, amc, or blackberry meme stonks. These are not your common stocks, they are special, meme stonks from Reddit, and we must always hold the line with our diamond hands!" 
elif float(latest_close) < 1.15 * recent_low:
    recommend = "Buy!"
    reason = "Nat-Bot thinks that this stock has a lot of potential based on how its less than fifteen percent more than its recent low."
elif float(latest_close) < 2 * recent_low:
    recommend = "Hold for now."
    reason = "Nat-Bot thinks that if you have the stock, keep it until it doubles its recent low, because it could still grow! If you don't have the stock, check for new updates daily in case it falls."
else:
    recommend = "Sell!"
    reason = "Nat-Bot sees that the stock has more than doubled from its recent low. This is a good time to sell it if you have it, or wait it out if you don't."


#cvs code here is from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
headers = ["timestamp", "open", "high", "low", "close", "volume"]

#this part is largely inspired by https://colab.research.google.com/drive/1EH3xNXPrO4dniIW12X9ATDz1lMyMBREb?usp=sharing
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]})


# this section, minus the variables, is from https://github.com/prof-rossetti/intro-to-python/blob/master/projects/robo-advisor/README.md
print("-------------------------")
print("SELECTED SYMBOL: ", symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
#used this next line from my shopping cart project
print("REQUEST COMPLETED AT: ", now.strftime('%I:%M %p'), "on", now.strftime('%b %d, %Y'))
print("-------------------------")
print("LATEST DAY: ", last_refreshed)
print("LATEST CLOSE: ", to_usd(float(latest_close)))
print("RECENT HIGH: ", to_usd(float(recent_high)))
print("RECENT LOW: ", to_usd(float(recent_low)))
print("-------------------------")
print("Nat-Bot's Stock Advisor is now analyzing your stock:")
print("RECOMMENDATION: ", recommend)
print("RECOMMENDATION REASON: ", reason)
print("-------------------------")
print("Nat-Bot is sending over your data to a CSV")
print("Your data is here: ", csv_file_path)
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


#an attempt for data viz, its messy but got help from https://pythonspot.com/matplotlib-line-chart/
prices = []
for date in dates:
    price = tsd[date]["4. close"]
    prices.append(float(price))

plt.plot(dates, prices)
plt.title('Prices over Time for your Inputed Stock')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.grid(True)
plt.show()