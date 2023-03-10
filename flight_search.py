import requests
from flight_data import FlightData
import os
import pprint

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_HEADERS = {"apikey": os.environ["TEQUILA_API_KEY"]}


class FlightSearch:

    def get_destination_code(self, city_name):
        tequila_params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=TEQUILA_HEADERS, params=tequila_params)
        response.raise_for_status()
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": os.environ["TEQUILA_API_KEY"]}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No direct flights found for {destination_city_code}. Check with 1 stopover.")
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            try:
                data = response.json()["data"][0]
                pprint(data)
            except IndexError:
                print(f"No flights found for {destination_city_code} with 1 stopover.")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{destination_city_code} : {data['price']} €")
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{destination_city_code} : {data['price']} €")
            return flight_data







