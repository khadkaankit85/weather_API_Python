import requests
import json
api_key =""
city=input("Enter the name of the city: ")
link=f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
news=requests.get(link).json()
# print("Current temperature is:", news["current"]["temperature"],"Degrees Celsius.")
# print(news["current"]["weather_description"])
if "current" in news: 
    news_dict=dict(news["current"])
    for i, j in news_dict.items():
        print(i,":",j)
else:
    print("Failed to get the information for the location you have entered:( ")