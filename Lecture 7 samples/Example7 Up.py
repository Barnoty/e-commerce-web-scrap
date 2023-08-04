from datetime import datetime,timedelta
import math

# Let's define two datetime objects

time1 = "2022/10/17 06:00:00"
d_time1 = datetime.strptime(time1, '%Y/%m/%d %H:%M:%S')

time2 = "22-10-21+12:15:23"
d_time2 = datetime.strptime(time2, '%y-%m-%d+%H:%M:%S')

diff = d_time2 - d_time1
print("The diff is a timedelta object:", diff)

# Attributes of timedelta objects
print("Number of passed days:", diff.days)
print("Number of seconds (in 6 h 15 min 23 sec):", diff.seconds)
print("#########")


print("Number of totals seconds:", diff.total_seconds())
minutes = math.floor(diff.total_seconds() / 60)
print("Number of passed minutes:", minutes)

hours = math.floor(diff.total_seconds() / (60 * 60))
print("Number of passed hours:", hours)



