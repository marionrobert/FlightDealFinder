from flight_data import FlightData
import smtplib
import os

MY_EMAIL = os.environ["MY_EMAIL"]
GMAIL_SERVER = "smtp.gmail.com"
MY_PASSWORD = os.environ["MY_PASSWORD"]
EMAIL_TEST = os.environ["EMAIL_TEST"]

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, data: FlightData):
        message = f"Subject:Interesting price for {data.destination_city}\n\n" \
                  f"Price: {data.price} euros\n" \
                  f"From: {data.origin_city} - Airport: {data.origin_airport}\n" \
                  f"To: {data.destination_city} - Airport: {data.destination_airport}\n" \
                  f"Outbound Date: {data.out_date}\n" \
                  f"Inbound Date: {data.return_date}\n"
        print(message)
        if data.stop_overs > 0:
            message += f"\nFlight has {data.stop_overs} stop over, via {data.via_city}."
            print(message)
        with smtplib.SMTP(GMAIL_SERVER) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=EMAIL_TEST,
                                msg=f"{message}")
