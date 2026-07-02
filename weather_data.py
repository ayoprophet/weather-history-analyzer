###### C1
# Creating a Class to retrieve weather data for a selected event, location and date

import requests

class WeatherData:
    def __init__(self, latitude, longitude, month, day, year, years):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.years = years

        self.five_year_max_temperature = None
        self.five_year_min_temperature = None
        self.five_year_avg_temperature = None

        self.five_year_max_precipitation = None
        self.five_year_min_precipitation = None
        self.five_year_sum_precipitation = None

        self.five_year_max_wind_speed = None
        self.five_year_min_wind_speed = None
        self.five_year_avg_wind_speed = None

        #empty lists for API to fill them
        self.temperatures = []
        self.wind_speeds = []
        self.precipitations = []
##### C2 - Pulling data for the location
    def fetch_weather_data(self): #API requests for the selected location and date

        for historical_year in self.years:
            date = f"{historical_year}-{self.month:02d}-{self.day:02d}"

            url = (
                "https://archive-api.open-meteo.com/v1/archive"
                f"?latitude={self.latitude}"
                f"&longitude={self.longitude}"
                f"&start_date={date}"
                f"&end_date={date}"
                "&daily=temperature_2m_mean,wind_speed_10m_max,precipitation_sum"
                "&temperature_unit=fahrenheit"
                "&wind_speed_unit=mph"
                "&precipitation_unit=inch"
                "&timezone=America%2FNew_York"
            )
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()

                self.temperatures.append(data["daily"]["temperature_2m_mean"][0])
                self.wind_speeds.append(data["daily"]["wind_speed_10m_max"][0])
                self.precipitations.append(data["daily"]["precipitation_sum"][0])

                print(f"Data retrieved for {historical_year}.")
            else:
                print(f"Can't retrive data for {historical_year}: {response.status_code}")

    # Calculations for the five years max, min, and average for temperature, wind speed and precipitation

    def calculate_temperatures(self):
            self.five_year_max_temperature = max(self.temperatures)
            self.five_year_min_temperature = min(self.temperatures)
            self.five_year_avg_temperature = sum(self.temperatures) / len(self.temperatures)

    def calculate_wind_speeds(self):
            self.five_year_max_wind_speed = max(self.wind_speeds)
            self.five_year_min_wind_speed = min(self.wind_speeds)
            self.five_year_avg_wind_speed = sum(self.wind_speeds) / len(self.wind_speeds)

    def calculate_precipitations(self):
            self.five_year_max_precipitation = max(self.precipitations)
            self.five_year_min_precipitation = min(self.precipitations)
            self.five_year_sum_precipitation = sum(self.precipitations)