import pandas as pd
from datetime import  datetime
import matplotlib.pyplot as plt
#pick any date after January of 2010
#let's pretend that you had $1000 dollars to invest at that date
#how much would it be today if you have invested back then and sold in on 1st of April 2019
#remotely download the SPX index from your date to 1st of April 2019
#load the FTSE from the file, and select values from your date  to 1st of April 2019
#normalize the return of each index for "Close" column so you can calculate your total return at any given date
#"invest" $1000 dollars on your date and make sure that you show your total gain/loss at every date
#plot both "investments" in SPX and FTSE on the same graph with names of "US Returns" and "EUR Returns" respectively.



import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
from datetime import datetime
ticker ="^ftm_d"
fromDate ="2010/02/08"
toDate = "2019/04/01"
Spx= pd.read_csv("^ftm_d.csv",index_col=["Date"],parse_dates=True)
print(Spx)
Ftm= pd.read_csv("^ftm_d.csv",index_col=["Date"],parse_dates=True)
print(Ftm)

investment = 1000
Spx= Spx["Close"].values
index =Spx.index
Ftm =Ftm["Close"].values
index = Ftm.index
print(Spx)
print(index)
Spx["gspcNormalized"] = Spx["Close"]/Spx["Close"][0]
Spx["US Returns"] = investment*Spx["gspcNormalized"]
Ftm["gspcNormalized"] = Ftm["Close"]/Ftm["Close"][0]
Ftm["US Returns"] = investment*Ftm["gspcNormalized"]
print(Ftm,Spx)
join = Spx.join(Ftm,how="inner").dropna()
index =join.index
print(join.head())

plt.plot(index,Spx,'r--',label='EUR Returns')
plt.plot(index,Ftm,'g',label='US Returns')
plt.show()




