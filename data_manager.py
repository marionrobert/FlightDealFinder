import requests
import os

SHEETY_ENDPOINT = f"{os.environ['SHEETY_ENDPOINT']}/prices"
SHEETY_HEADERS = {"Authorization": os.environ["TOKEN"]}


class DataManager:
    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                headers=SHEETY_HEADERS,
                json=new_data
            )
            # print(response.text)
