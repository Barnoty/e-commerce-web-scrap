from matplotlib import pyplot as plt
import numpy as np
x=['Mon', 'Tue', 'Wed', 'Thurs']
dev1=np.arange(1,5,1)
dev2=np.arange(4,0,-1)
dev3=[3,1,4,2]

#Pie charts
#label=['a','b','c','d']
#plt.pie(dev1, labels=label)
#plt.legend()

labels=['Dev1', 'Dev2', 'Dev3']
plt.stackplot(x,dev1,dev2,dev3, labels=labels)

plt.title("Dev Performance over 4 days")
plt.legend(loc='lower right')
plt.xlabel("Days")
plt.ylabel('Hours worked')
plt.show()


