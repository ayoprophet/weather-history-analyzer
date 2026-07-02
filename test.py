import unittest

import weather_data
from weather_data import WeatherData

class TestWeatherData(unittest.TestCase):

# Test 1: testing the WeatherData object stores location and date correctly
    def test_weather_data_created(self):

        weather = WeatherData(40.8584, -74.1638, 6, 1, 2026, [2021, 2022, 2023, 2024, 2025])

        self.assertEqual(weather.latitude, 40.8584)
        self.assertEqual(weather.longitude, -74.1638)
        self.assertEqual(weather.month, 6)
        self.assertEqual(weather.day, 1)
        self.assertEqual(weather.year, 2026)
        self.assertEqual(weather.years, [2021, 2022, 2023, 2024, 2025])

# Test 2: testing the temperature statistic are calculated correctly.

    def test_calculate_temperatures(self):

        weather = WeatherData(40.8584, -74.1638, 6, 1, 2026, [2021, 2022, 2023, 2024, 2025])
        weather.temperatures = [60.0, 65.0, 70.0, 75.0, 80.0]

        weather.calculate_temperatures()

        self.assertEqual(weather.five_year_max_temperature, 80.0)
        self.assertEqual(weather.five_year_min_temperature, 60.0)
        self.assertEqual(weather.five_year_avg_temperature, 70.0)

# Test 3: testing the precipitation statistics are calculated correctly.

    def test_calculate_precipitation(self):

        weather = WeatherData(40.8584, -74.1638, 6, 1, 2026, [2021, 2022, 2023, 2024, 2025])
        weather.precipitations = [0.0, 0.2, 0.1, 0.4, 0.3]

        weather.calculate_precipitations()

        self.assertEqual(weather.five_year_max_precipitation, 0.4)
        self.assertEqual(weather.five_year_min_precipitation, 0.0)
        self.assertEqual(weather.five_year_sum_precipitation, 1.0)

if __name__ == "__main__":
    unittest.main()


