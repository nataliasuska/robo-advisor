# Nat-Bot Stock Advisor
The Nat-Bot is now a robo advisor capable of providing automated stock trading recommedations*. This program can accept one or more stock or crypto symbols as inputs, then it will request live historical trading data from the internet using an API from Alpha Vantage, and finally provide a reommendaton as to whether or not you or a client should purchase the given stock or cryptocurrency. We also have special features that send historical prices of your inputted stock into a CSV, and a line graph to see historical prices of that stock over time.

*Note that neither I nor this program are financial advisors.

## Required
+ Anaconda 3.7+
+ Python 3.7+
+ Pip

## User Instructions
### Cloning
Fork this remote repository under your own control, and then clone it by your own preferences (ZIP folder, command-line, or using GitHub Desktop software). Upon completion, choose a familiar download location - I use my Desktop. 

## Environment Setup
After cloning this repo, navigate to it from your command line. Since I just put it in my desktop, it will look like this for me, but may look different for you:
```sh
cd ~/Desktop/robo-advisor
```
Create and activate a new project-specific Anaconda virtual environment for our project titled stocks-env (but you can use a different title), and activate it:
```sh
conda create -n stocks-env python=3.8
conda activate stocks-env
```
From inside of our virtual environment, install the package requirements:
```sh
pip install -r requirements.txt
```

## API Key 
In our root directory of the repository, create a file called .env to store our API key. In the file, input:
```
ALPHAVANTAGE_API_KEY = "123"
```
We will now replace the 123 with the actual key.

To set up an API, go to [the Alpha Vantage website](https://www.alphavantage.co/) and claim your free API key. Follow the instructions, and receive a key code. Copy and paste it into your .env file to replace the 123 in our environment variable.


## Run the Code
Now let's run the Python script from the command-line:
```sh
python app/robo_advisor.py
```
We will first be promtpted to type in a stock or cryptocurrency ticker. Please input a valid ticker between 1-5 letters, and without any numbers or other characters. Lower or uppercase is fine. 

If the stock is valid, a pop-up graph appears. It is a line graph showing the historical prices over time of the inputted stock. Save it if desired, but please close it so that the Nat Bot can finish her stock recommendation.

Upon closing the graph, the Nat Bot will display some information for the stock including when this particular request occured, the latest day the stock price was updated, the latest closing price, and a recent high and low. This Nat Bot is also equipped with providing a stock's buy, sell, or holding recommendation and explanation. For reference:
+ Buy! = Nat-Bot thinks that this stock has a lot of potential based on how its less than 15% above its recent low.
+ Hold for now. = Nat-Bot thinks that if you have the stock, you should keep it until it doubles its recent low price, because it could still grow! If you don't have the stock, check for new updates daily in case it falls.
+ Sell! = Nat-Bot sees that the stock has more than doubled from its recent low price. This is a good time to sell it if you have it, or wait it out if you don't.
+ DIAMOND HANDS!!! = This is an extra special case. Nat-Bot sees that you have chosen either gamestop, amc, or blackberry meme stonks as your input. These are not your common stocks, they are meme stonks from Reddit ([see r/wallstreetbets](https://www.reddit.com/r/wallstreetbets/)). We must *always* hold the line with our diamond hands!

Finally, the Nat Bot will send over historical stock prices of the inputted stock onto a CSV file within the data folder part of the repo. The location will also be shown where the Nat-Bot says "Your data is here: .." Keep in mind that this file will be ignored when commiting to github. 