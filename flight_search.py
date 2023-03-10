import requests
import os

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
TEQUILA_HEADERS = {"apikey": TEQUILA_API_KEY}


class FlightSearch:

    def get_destination_code(self, city_name):
        tequila_params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
        }
        response = requests.get(url=TEQUILA_ENDPOINT, headers=TEQUILA_HEADERS, params=tequila_params)
        response.raise_for_status()
        results = response.json()["locations"]
        code = results[0]["code"]
        return code






