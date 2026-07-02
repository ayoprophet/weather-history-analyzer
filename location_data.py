import requests

##Using the Open-meteo API to find latitude and longitude for a city

def get_location_coordinates(city_name, state_or_country):

    url = ("https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city_name}"
        "&count=10"
        "&language=en"
        "&format=json")

    response = requests.get(url)

    if response.status_code != 200:
        print("City not found")
        return None
    data = response.json()

    if "results" not in data:
        print("No location found.")
        return None

    results = data["results"]

    for location in results:
        location_t = f"{location.get('name', '')} {location.get('admin1', '')} {location.get('country', '')}"

        if state_or_country.lower() in location_t.lower():
            return {"name": location.get("name"),
                    "state": location.get("admin1"), #admin1 means state/region/province on Open-meteo
                    "country": location.get("country"),
                    "latitude": location.get("latitude"),
                    "longitude": location.get("longitude")}
    first_result = results[0]
    return {"name": first_result.get("name"),
            "state": first_result.get("admin1"),
            "country": first_result.get("country"),
            "latitude": first_result.get("latitude"),
            "longitude": first_result.get("longitude")
    }