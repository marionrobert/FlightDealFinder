import requests

SHEETY_ENDPOINT = "https://api.sheety.co/075a1aa8ceadab13ed826945168b2fff/flightDeals/prices"
SHEETY_HEADERS = {"Authorization": "Bearer erg4es64fd^dfnhf"}

class DataManager:
    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
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
