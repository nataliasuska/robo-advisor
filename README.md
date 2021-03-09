# Nat-Bot Stock Advisor
The Nat-Bot is now a robo advisor capable of providing automated stock trading recommedations*. This program can accept one or more stock or crypto symbols as inputs, then it will request live historical trading data from the internet, and finally provide a reommendaton as to whether or not you or a client should purchase the given stock or cryptocurrency.

*Note that neither I nor this program are financial advisors.

## Required
+ Anaconda 3.7+
+ Python 3.7+
+ Pip
+ A command-line terminal (I use Git Bash for windows)

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
ALPHAVANTAGE_API_KEY="123"
```
We will now replace the 123 with the actual key.

For setting up our API, go to [the Alpha Vantage website](https://www.alphavantage.co/) and claim your free API key. Follow the instructions, and receieve a key code. Copy and paste it into your .env file to replace the 123 in our environment variable.


## Checkout - Run the Code
Now let's run the Python script from the command-line:
```sh
python app/robo_advisor.py
```