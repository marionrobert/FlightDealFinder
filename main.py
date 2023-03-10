from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)


if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()