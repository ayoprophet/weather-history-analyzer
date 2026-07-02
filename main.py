#importing WeatherData from weather_data.py
from weather_data import WeatherData
from secondclassSQL import save_weather_data, query_weather_data
from location_data import get_location_coordinates

print("Starting Weather History Analyzer...\n ")

## User inputs for location and event date

city_name = input("Enter city name: ")
state_or_country = input("Enter state or country: ")

month = int(input("Enter Month as a number: "))
day = int(input("Enter Day: "))
year = int(input("Enter Year: "))

##Calculate the previous five years

years = [year - 5, year - 4, year - 3, year - 2, year - 1]

location = get_location_coordinates(city_name, state_or_country)

if location is None:
    print("Location not found.")
else:
    latitude = location["latitude"]
    longitude = location["longitude"]

    print("\n Location Found")

    print(f"City: {location['name']}")
    print(f"State: {location['state']}")
    print(f"Country: {location['country']}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    print("\nSelected Event Information...")
    print(f"Data: {month}/{day}/{year}")
    print(f"Historical Years: {years}")

    ## Calling the methods used in Weather_data
    location_weather = WeatherData(latitude, longitude, month, day, year, years)
    print("WeatherData object created successfully.")

    location_weather.fetch_weather_data()
    location_weather.calculate_temperatures()
    location_weather.calculate_wind_speeds()
    location_weather.calculate_precipitations()

    print("Weather Data gathered from Open Meteo API...")
    print("5 Year Statistics successfully calculated...")

    ## Saving calculated weather data in SQLite database
    save_weather_data(location_weather)
    print("Weather data saved to the SQLite Database...")

    ## Query the table created in SQLite and display the data
    print("Querying stored weather data from SQLite database...")

    query_weather_data()

    print("Application completed successfully.")



