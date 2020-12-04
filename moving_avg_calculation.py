from send_message import send_message, send_pic
#send_message("daca merge si asta... chiar sunt tare!")

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

TICKER = pd.read_csv("prices/EPD.csv")

#visualize data

plt.figure(figsize=(12.5, 4.5))
plt.plot(TICKER['Adj Close'], label="EPD")
plt.title("Istoricul Enterprise Products Partners L.P.  (EPD)")
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
plt.plot(TICKER['Adj Close'], label="EPD")
plt.plot(SMA30['Adj Close'], label='SMA30')
plt.plot(SMA100['Adj Close'], label='SMA100')

plt.title("Istoricul Enterprise Products Partners L.P.  (EPD)")
plt.xlabel('Jul 1998 - Dec 2020')
plt.ylabel('Pretul final de zi ($)')
plt.legend(loc='upper left')
#plt.show()

#create new data frame to store all the data
data = pd.DataFrame()
data['EPD'] = TICKER['Adj Close']
data['SMA30'] = SMA30['Adj Close']
data['SMA100'] = SMA100['Adj Close']

print(data)
