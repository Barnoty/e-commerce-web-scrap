import json
from urllib.request import *

file=urlopen("https://api.open-meteo.com/v1/forecast?latitude=0.9138&longitude=35.7387&hourly=temperature_2m")
content=file.read()

lj=json.loads(content)

print(lj["latitude"],">>",lj["longitude"])

for i in range(1,len(lj["hourly"]['time'])):
    print(lj["hourly"]['time'][i], ">>",lj["hourly"]['temperature_2m'][i])
