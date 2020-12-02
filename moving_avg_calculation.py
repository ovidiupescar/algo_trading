from send_message import send_message, send_pic
#send_message("daca merge si asta... chiar sunt tare!")

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

TICKER = pd.read_csv("prices/ZM.csv")

#visualize data

plt.figure(figsize=(12.5, 4.5))
plt.plot(TICKER['Adj Close'], label="ZM")
plt.title("Istoricul Zoom (ZM)")
plt.xlabel('Dec 2019 - Dec 2020')
plt.ylabel('Pretul final de zi ($)')
plt.legend(loc='upper left')


fig = plt.subplot()
fig.savefig("diagrams/ZMe.png")
plt.show()
