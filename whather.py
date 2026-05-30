city = input("Enter the city name: ")
temp = float(input("Enter the temperature in Celsius: "))
if temp > 30:
    print(f"The weather in {city} is hot.")
if temp > 25:
    print("great day to go outside")
else:
    print("grab a jacket beforegoing outside`")
if temp > 15:
        print("but it is not too cold")
elif temp > 20:
    print(f"The weather in {city} is warm.")
elif temp > 10:
    print(f"The weather in {city} is cool.")
else:
    print(f"The weather in {city} is cold.")
import datetime
import calendar
now = datetime.datetime.now()
print(f"City: {city}")
print("time now:",now)
print(calendar.calendar(now.year))