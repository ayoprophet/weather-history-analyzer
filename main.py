#####C1
#importing WeatherData from weather_data.py
from weather_data import WeatherData
from secondclassSQL import save_weather_data, query_weather_data

# Location and date: Clifton, New jersey on June 1st
latitude = 40.8584
longitude = -74.1638
month = 6
day = 1
year = 2026
years = [2021, 2022, 2023, 2024, 2025]

print("Starting Weather Prediction Application...\n ")
print("Selected Location and Date")
print(f"Clifton, New Jersey")
print(f"Latitude: {latitude}, Longitude: {longitude}")
print(f"Month: {month}, Day: {day}, Year: {year}")


# An instance of Weather Data class.
## C2 - C3 - Calling the methods used in Weather_data
location_weather = WeatherData(latitude, longitude, month, day, year, years)
print("WeatherData object created successfully.")

location_weather.fetch_weather_data()
location_weather.calculate_temperatures()
location_weather.calculate_wind_speeds()
location_weather.calculate_precipitations()

print("Weather Data gathered from Open Meteo API...")
print("5 Year Statistics successfully calculated...")


#### C5: Saving calculated weather data in SQLite database
save_weather_data(location_weather)
print("Weather data saved to the SQLite Database...")

#### C6: Query the table created in SQLite and display the data

print("Querying stored weather data from SQLite database...")

query_weather_data()

print("Application completed successfully.")

