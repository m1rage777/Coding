


weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}

sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
snowing_weather = {key: value for (key,value) in weather.items() if value == "snowing"}
cloudy_weather = {key: value for (key,value) in weather.items() if value == "cloudy"}

print(sunny_weather,snowing_weather,cloudy_weather)


# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)
