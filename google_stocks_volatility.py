#
# How Google stock price Volatility has
#  fluctuated over the years
#
#


## Import libraries

import numpy as np
import pandas as pd

import pandas_datareader as pdr
import pandas_datareader.data as web

import matplotlib.pyplot as plt

import datetime as dt


print("pandas_datareader version = " + pdr.__version__)
print("Numpy version = " + np.__version__)

# Read Google stocks data 

sdate = dt.datetime(2009, 3, 14)
edate = dt.datetime(2017, 12, 30)

goog = web.DataReader('GOOG', 'google', sdate, edate)

print( goog.tail())

goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
goog['Volatility'] = pd.rolling_std(goog['Log_Ret'], window=252) * np.sqrt(252)

#%matplotlib inline
goog[['Close', 'Volatility']].plot(subplots=True, color='blue', figsize=(8, 6))

plt.show()
