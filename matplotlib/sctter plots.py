import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

df=pd.read_csv('youtube stats.csv')

views=df['view_count']
likes=df['likes']
ratio=df['ratio']

plt.scatter(views, likes, c=ratio, cmap='summer',
            edgecolors='black', linewidths=1, alpha=0.75)

cbar=plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')


plt.title('Corey Shafer Youtube Stats')
plt.tight_layout
#plt.legend()
plt.show()

