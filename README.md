# Scripting and Programming - Applications — D493

# Weather Prediction Application

## Project Description

This python project is a weather prediction application created for WGU Scripting and Programming - Applications performance assessment.

The application collects historical weather data for a selected event location and date using the Open Meteo Weather API.
The program calculates five-year weather statistics for temperature, wind speed and precipitation and stores the results in a local SQLite database using SQLAlchemy ORm and queries the database to display the stored weather data. 

## Scenario

Clifton, NJ is the selected location for this project. The selected date is June 1, 2026.
The program retrieves historical weather data for June 1 from the previous five complete years:
2021, 2022, 2023, 2024, and 2025

The purpose of collecting this data is to support event planning decisions, such as planning trips, marketing certain summer products, etc. based on historical temperature, wind speed and precipitation conditions.

## Location and Date Inputs

- Location: Clifton, New Jersey
- Latitude: 40.8584
- Longitude: -74.1638
- Event Month: 6
- Event Day: 1
- Event Year: 2026
- Historical Years: 2021, 2022, 2023, 2024, 2025

## Weather Variables Retrieved 

- Mean temperature in Fahrenheit
- Maximum wind speed in mph
- Precipitation sum in inches

## Weather Statistics Calculated

- Five-year average temperature
- Five-year minimum temperature
- Five-year maximum temperature
- Five-year average wind speed
- Five-year minimum wind speed
- Five-year maximum wind speed
- Five-year minimum precipitation
- Five-year maximum precipitation
- Five-year sum precipitation

## Project Files

- 'main.py' - runs the program, creates the WeatherData object, calls weather methods, saves data to the database, and queries the stored data.
- 'weather_data.py' - contains the WeatherData class used to retrieve and calculate weather statistics.
- 'secondclassSQL.py' - contains the SQLAlchemy ORM table class and database functions.
- 'secondclass.db' - SQLite database file created by the program
- 'test.py' - contains three unit tests for the program.
- 'requirements.txt' - Lists the required packages and versions

## Commands to Run the Program

You can use bash by typing this command:

python main.py
python test.py

Or

You can simply use run button located at the top.
