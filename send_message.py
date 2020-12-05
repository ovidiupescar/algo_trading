import telegram_send
"""
###########################################
### Example of diagram send to Telegram ###
###########################################

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Diagrama de test!!')
ax.grid()

fig.savefig("test.png")
plt.show()

with open("test.png", "rb") as f:
    telegram_send.send(images=[f])
"""

def send_message(message):
    telegram_send.send(messages=[message])

def send_pic(img):
    with open(img, "rb") as f:
        telegram_send.send(images=[f])
