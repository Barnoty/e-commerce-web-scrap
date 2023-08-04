import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates

df=pd.read_csv('BTC rates.csv')  #import
df['Date']=pd.to_datetime(df['Date']) #conver Date column to datetime
df.sort_values('Date', inplace=True) #Sort using Date column & save

dates=df['Date']
trading_close=df['Close']

plt.plot_date(dates, trading_close, linestyle='solid') #plot

plt.gcf().autofmt_xdate() #Format date to display better and takes in no parameters

date_format=mpl_dates.DateFormatter('%b, %d %Y') #Format date accord to desired datetime format
plt.gca().xaxis.set_major_formatter(date_format)

plt.title('BTC Daily Closing price')
plt.xlabel('Dates')
plt.ylabel('Daily Close price')
plt.tight_layout
plt.show()