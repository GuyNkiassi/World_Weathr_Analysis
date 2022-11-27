# Use the citipy module to determine city based on latitude and longitude.
# Import initial libraries
import numpy as np
import pandas as pd
# Import the OpenWeatherMap's API key
from config import weather_api_key

# Import the requests library
import requests


# Import the time library
import time
from datetime import datetime

cities = []

cities.append("Boston") # YOUR CODE HERE

# Print the city count to confirm sufficient count
print(len(cities)) # YOUR CODE HERE

#cities = ["A","B","C"]
print(list(enumerate(cities)))

for i, city in enumerate(cities):
    print(i,city)


# Create an empty list to hold weather data for each city
city_data = []

# Print a message to indicate that the data retrieval starts
print("Beginning Data Retrieval     ")
print("-----------------------------")

# Create counters and set them to 1
record_count = 1
set_count = 1

# Loop through all the cities in our list to fetch weather data for each city
for i, city in enumerate(cities):
        
    # Group cities in sets of 50 for logging purposes
    if (i % 50 == 0 and i >= 50):
        set_count += 1
        record_count = 1
#         time.sleep(60)

    # Create an endpoint URL for each city
    url = f'http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID={weather_api_key}&q={city}'
    
    # Log the url, record, and set numbers
    #print(f"Processing Record {record_count} of Set {set_count} | {city}")

    # Add 1 to the record count
    record_count += 1

    # Run an API request for each of the cities
    try:
        city_weather = requests.get(url).json()

        print(city_weather['sys']['country'])
        city_data.append( {'City' : "Testabc",
                         'Country' : city_weather['sys']['country']})
        print(city_data)
        print(len(city_data)+100000)
        print(city_weather['dt'])
        date_time = datetime.fromtimestamp(city_weather['dt'])
        print(date_time.strftime('%m/%d/%Y, %H:%M:%S'))

        print(datetime.fromtimestamp(city_weather['dt']).strftime('%Y-%m-%d, %H:%M:%S'))
        # Parse out the latitude, longitude, max temp, humidity, cloudiness, wind, country, and weather description
        # YOUR CODE HERE   
        city_data.append({
            'City': city,
            'Country': city_weather['sys']['country'],
            'Date': city_weather['dt'],
            #'Date': datetime.fromtimestamp(city_weather['dt']).strftime('%Y-%m-%d %H:%M:%S'),
            'Lat': city_weather["coord"]["lat"],
            'Lng':  city_weather["coord"]["lon"],
            'Max Temp': city_weather["main"]["temp_max"],
            'Humidity': city_weather["main"]["humidity"],
            'Cloudiness': city_weather["clouds"]["all"],
            'Wind Speed': city_weather["wind"]["speed"]
        })
        
        # If an error is experienced, skip the city
    except:
        #print("City not found. Skipping...")
        pass

# Indicate that the data retrieval is complete 
print("-----------------------------")
print("Data Retrieval Complete      ")
print("-----------------------------")

print(city_data)
print(len(city_data))