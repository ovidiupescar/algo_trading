from send_message import send_message, send_pic
#send_message("daca merge si asta... chiar sunt tare!")

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

TICKER = pd.read_csv("prices/BA.csv")

#visualize data

plt.figure(figsize=(12.5, 4.5))
plt.plot(TICKER['Adj Close'], label="BA")
plt.title("Istoricul Enterprise Products Partners L.P.  (BA)")
plt.xlabel('Jul 1998 - Dec 2020')
plt.ylabel('Pretul final de zi ($)')
plt.legend(loc='upper left')

#plt.show()

#create the simple moving average with a 30 day window

SMA30 = pd.DataFrame()
SMA30['Adj Close'] = TICKER['Adj Close'].rolling(window=30).mean()
#print(SMA30)

#Create a simple moving 100 day average
SMA100 = pd.DataFrame()
SMA100['Adj Close'] = TICKER['Adj Close'].rolling(window=100).mean()
#print(SMA100)

#Visualize the data

plt.figure(figsize=(12.5, 4.5))
plt.plot(TICKER['Adj Close'], label="BA")
plt.plot(SMA30['Adj Close'], label='SMA30')
plt.plot(SMA100['Adj Close'], label='SMA100')

plt.title("Istoricul Enterprise Products Partners L.P.  (BA)")
plt.xlabel('Jul 1998 - Dec 2020')
plt.ylabel('Pretul final de zi ($)')
plt.legend(loc='upper left')
plt.show()

#create new data frame to store all the data
data = pd.DataFrame()
data['BA'] = TICKER['Adj Close']
data['SMA30'] = SMA30['Adj Close']
data['SMA100'] = SMA100['Adj Close']

#create a function to signal when to buy and sell

def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1

    for i in range(len(data)):
        if data['SMA30'][i] > data['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(data['BA'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['SMA30'][i] < data['SMA100'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['BA'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return (sigPriceBuy, sigPriceSell)

#store buy sell into a variable

buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

#show the data
print(data)

plt.figure(figsize=(12.5, 4.5))
plt.plot(data['BA'], label="BA", alpha=0.35)
plt.plot(data['SMA30'], label='SMA30', alpha=0.35)
plt.plot(data['SMA100'], label='SMA100', alpha=0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label='Buy', marker='^', color='green')
plt.scatter(data.index, data['Sell_Signal_Price'], label='Sell', marker='v', color='red')
plt.title("Istoricul BA")
plt.xlabel('Jul 1998 - Dec 2020')
plt.ylabel('Pretul final de zi ($)')
plt.legend(loc='upper left')
plt.show()
