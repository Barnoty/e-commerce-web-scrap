import pandas as pd
from matplotlib import pyplot as plt

#plt.style.use('fivethirtyeight')

df=pd.read_csv('mean dev salaries.csv')

ages=df['Age']
bins=[10,20,30,40,50,60,70,80,90,100]
plt.hist(ages, bins=bins, edgecolor='black', log=True, color='green', alpha=0.25)


median_age=29
plt.axvline(median_age,color='red', label='Median Age', linewidth=2 )



plt.title('Developer Age groups Histogram')
plt.tight_layout
plt.legend()
plt.show()

