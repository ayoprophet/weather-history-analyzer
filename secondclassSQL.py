###C4 -- CREATING SECOND CLASS (SQLite, SQLAlchemy Orm Module) --

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker


base = declarative_base()

#### C4: Creating SQLite table:

class WeatherRecord(base):

    __tablename__ = 'weather_records'

    id = Column(Integer, primary_key=True, autoincrement=True)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)

    five_year_max_temperature = Column(Float)
    five_year_min_temperature = Column(Float)
    five_year_avg_temperature = Column(Float)

    five_year_max_wind_speed = Column(Float)
    five_year_min_wind_speed = Column(Float)
    five_year_avg_wind_speed = Column(Float)

    five_year_max_precipitation = Column(Float)
    five_year_min_precipitation = Column(Float)
    five_year_sum_precipitation = Column(Float)

engine = create_engine('sqlite:///secondclass.db')
base.metadata.drop_all(engine)
base.metadata.create_all(engine)

####C5 : Inserting database records:

Session = sessionmaker(bind=engine)
session = Session()

def save_weather_data(weather_data):

    weather_record = WeatherRecord(
        latitude = weather_data.latitude,
        longitude = weather_data.longitude,
        month = weather_data.month,
        day = weather_data.day,
        year = weather_data.year,

        five_year_max_temperature = weather_data.five_year_max_temperature,
        five_year_min_temperature = weather_data.five_year_min_temperature,
        five_year_avg_temperature = weather_data.five_year_avg_temperature,

        five_year_max_wind_speed = weather_data.five_year_max_wind_speed,
        five_year_min_wind_speed= weather_data.five_year_min_wind_speed,
        five_year_avg_wind_speed= weather_data.five_year_avg_wind_speed,

        five_year_max_precipitation= weather_data.five_year_max_precipitation,
        five_year_min_precipitation= weather_data.five_year_min_precipitation,
        five_year_sum_precipitation=weather_data.five_year_sum_precipitation

    )
    session.add(weather_record)
    session.commit()

#### C6 Query the table created in SQLite and retrieve the data

def query_weather_data():

    weather_records = session.query(WeatherRecord).all()

    if weather_records:

        print(f"\nFound {len(weather_records)} weather record(s)")

        for weather_record in weather_records:

            print(f"Record ID: {weather_record.id}")
            print(f"Location Latitude: {weather_record.latitude}")
            print(f"Location Longitude: {weather_record.longitude}")
            print(f"Date: {weather_record.month}/{weather_record.day}/{weather_record.year}")

            print(f"\nTemperature Statistics")
            print(f"Five-Year Maximum Temperature: {weather_record.five_year_max_temperature:.2f} °F")
            print(f"Five-Year Minimum Temperature: {weather_record.five_year_min_temperature:.2f} °F")
            print(f"Five-Year Average Temperature: {weather_record.five_year_avg_temperature: .2f} °F" )

            print(f"\nWind Speed Statistics")
            print(f"Five-Year Maximum Wind Speed: {weather_record.five_year_max_wind_speed: .2f} mph")
            print(f"Five-Year Minimum Wind Speed: {weather_record.five_year_min_wind_speed: .2f} mph")
            print(f"Five-Year Average Wind Speed: {weather_record.five_year_avg_wind_speed: .2f} mph")

            print(f"\nPrecipitation Statistics")
            print(f"Five-Year Maximum Precipitation: {weather_record.five_year_max_precipitation:.2f} inches")
            print(f"Five-Year Minimum Precipitation: {weather_record.five_year_min_precipitation:.2f} inches")
            print(f"Five-Year Sum Precipitation: {weather_record.five_year_sum_precipitation:.2f} inches")
    else:
        print("No weather records found.")