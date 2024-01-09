# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
#print (len(weatherdata))
warmday = max(weatherdata, key = lambda x:x["tmax"])
print (warmday)

# TODO: What was the coldest day in the data set?
#print (weatherdata[0])
min_temperatures = {}
for item in weatherdata:
    key = item["date"]
    value = item["tmin"]
    min_temperatures[key] = value

coldest_temperature = min(min_temperatures.values())
coldest_day = min(min_temperatures, key = min_temperatures.get)

print (f"Coldest day is {coldest_day} with minimum temperature of {coldest_temperature} degree Fahrenheit.")

snowfall_days=0
# TODO: How many days had snowfall?
for item in weatherdata:
    key = item["date"]
    value = item["snow"]
    if value>0.0:
        snowfall_days+=1

print ("Number of days with snowfall = ", snowfall_days)

snowdays = [day for day in weatherdata if day["snow"]>0]
print (len(snowdays))