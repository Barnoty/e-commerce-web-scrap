from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight') #styling

#plt.xkcd() #Comic antigravity style

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
all_devs = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
# Median Python Developer Salaries by Age
py_devs = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
# Median JavaScript Developer Salaries by Age
js_devs = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]



#instantiate fig 1
fig1, (ax1, ax2) =plt.subplots(2,1, sharex=True)


#First plot
ax1.plot(ages_x,all_devs, color='red', label='All Devs')
ax1.set_title("Median Salary (USD) by Age")
ax1.set_ylabel("Median Salary")
ax1.legend(loc='upper left')

#Second plot
ax2.plot(ages_x, py_devs, color='blue', label='Python Devs')
ax2.plot(ages_x, js_devs, color='green', label='JS Devs')

ax2.set_xlabel("Ages")
ax2.set_ylabel("Median Salary")
ax2.legend(loc='upper left')


#instantiate fig 2
fig2, ax3 =plt.subplots()
ax3.plot(ages_x, py_devs, label='Fig 2 python')
ax3.set_title(" Fig 2 Median Salary (USD) by Age")
ax3.set_xlabel("Fig 2 Ages")
ax3.set_ylabel("Fig 2 Median Salary")
ax3.legend(loc='upper left')


# General functions
plt.tight_layout()
plt.grid(True)
plt.show()