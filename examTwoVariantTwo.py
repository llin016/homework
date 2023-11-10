#1.In this assignment, you will analyze the performance of one of the best performing mutual fund -- Fidelity Magellan Fund (FMAGX) and gold.
#2.Your task is to compare the risk/returns of these assets over a three-year period, from January 1st, 2019 to January 1st, 2022.
#3.To do this, you will need to remotely download the historical prices for fund from a financial data
# source of your choice  and normalize the returns to day 0, where the value on January 1st, 2019, will be 1.0.
#4.Once you have normalized the data, you will calculate standard deviation for the fund.
#5. Using this information, create two new columns for the fund, showing the normalized prices plus and  minus two standard deviations.
#6.Next, you will load data from a CSV file containing the historical prices(aur-hist.csv) of gold over
# the same three-year period(NOTE THIS, DATA IS FOR 10 YEARS SO YOU NEED TO LIMIT YOUR DATA BEFORE CALCULATING STD)
# Normalize the data to day 0, calculate standard deviation,and create the same plus and minus two standard deviation columns.
#7.Finally, you will plot the modified data for two assets on the same graph(two lines per asset(+/- std), with the dates on
# the x-axis and the normalized prices on the y-axis. Additionally, you will add a horizontal line at 1.00 to indicate the starting value of each asset.
#8.Your goal is to demonstrate your proficiency in using pandas to work with remote financial data
#sources, modifying the data, and creating effective visualizations to aid in interpreting the data. Good luck!

import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
from datetime import datetime

mage= pd.read_csv("FMAGX.csv",index_col=["Date"],parse_dates=True)
print(mage)

mageOpen = mage.Open
normalizedOpen = (mageOpen - mageOpen.min()) / (mageOpen.max() - mageOpen.min())
openMean = normalizedOpen.mean()
openVariance = normalizedOpen.std()
values = mageOpen.values
values = values [1:]

plt.hist(values, 500, facecolor = "blue", alpha =0.5)


plt.axvline(x=openMean)
plt.axvline(x=openMean+2*openVariance)
plt.axvline(x=openMean-2*openVariance)
plt.show()

#plt.axvline(x=mean)
#plt.axvline(x=mean+2*variance)
#plt.axvline(x=mean-2*variance)

mageHigh = mage.High
normalizedHigh = (mageHigh - mageHigh.min()) / (mageHigh.max() - mageHigh.min())
highMean = normalizedHigh.mean()
highVariance = normalizedHigh.std()

plt.axvline(x=highMean)
plt.axvline(x=highVariance+2*highVariance)
plt.axvline(x=highMean-2*highVariance)

mageLow = mage.Low
normalizedLow = (mageLow - mageLow.min()) / (mageLow.max() - mageLow.min())
lowMean = normalizedLow.mean()
lowVariance =normalizedLow.std()
plt.axvline(x=lowMean)
plt.axvline(x=lowMean+2*lowVariance)
plt.axvline(x=lowMean-2*lowVariance)

mageClose = mage.Close
normalizedClose = (mageClose - mageClose.min()) / (mageClose.max() - mageClose.min())
closeMean = normalizedClose.mean()
closeVariance = normalizedClose.std()

plt.axvline(x=closeMean)
plt.axvline(x=closeMean+2*closeVariance)
plt.axvline(x=closeMean-2*closeVariance)

mageAdjClose = mage[["Adj Close"]]
normalizedAdjClose = (mageAdjClose - mageAdjClose.min()) / (mageAdjClose.max() - mageAdjClose.min())
AdjCloseMean = normalizedAdjClose.mean()
AdjCloseMeanVariance = normalizedAdjClose.std()
plt.axvline(x=AdjCloseMean)
plt.axvline(x=AdjCloseMean+2*AdjCloseMeanVariance)
plt.axvline(x=AdjCloseMean-2*AdjCloseMeanVariance)
plt.show()


fromDate = "2019-01-01"
toDate = "2022-01-01"
data = web.DataReader('ARU','yahoo',fromDate,toDate)
print(data)

mage = mage[["Close"]]
mage['pctChange'] = mage["Close"].pct_change()
mage = mage.drop("Close",axis=1)

values = mage['pctChange'].values
values = values[1:]
print(mage)

plt.hist(values,50,facecolor='b',alpha=0.3)
#plt.show()

mean = mage['pctChange'].mean()
#print(mean)
variance = mage['pctChange'].std()
#print(variance)

plt.axvline(x=mean)
plt.axvline(x=mean+2*variance)
plt.axvline(x=mean-2*variance)


#plt.show()

#normalized_mage = (mage - mage.min()) / (df.max() - df.min())

