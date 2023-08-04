import pandas as pd
from matplotlib import pyplot as plt

#plt.style.use('fivethirtyeight')

df=pd.read_csv('mean dev salaries.csv')

ages_x=df['Age']
all_devs=df['All_Devs']
python_devs=df['Python']
js_devs=df['JavaScript']

plt.plot(ages_x,python_devs, label='Python Devs')
plt.plot(ages_x,all_devs, label='All Devs')


plt.fill_between(ages_x,python_devs, all_devs,
                 where=(python_devs > all_devs),
                 interpolate=True, alpha=0.25, label='More than Devs')

plt.fill_between(ages_x,python_devs, all_devs,
                 where=(python_devs <= all_devs),
                 interpolate=True, color='red', alpha=0.25, label='Less than Devs')

plt.title('Developer Mean salaries')
plt.tight_layout
plt.legend()
plt.show()

