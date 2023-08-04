from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight') #styling

df=pd.read_csv('ETH monthly Highs.csv')
high=df['high']

date=df['Date']

plt.barh(date,high)
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()


