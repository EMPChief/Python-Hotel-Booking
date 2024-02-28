import pandas as pd
import datetime


class ReservationTicket:
    def __init__(self, hotel_id, customer_name, customer_last_name, stay_time, db_path=None):
        self.hotel_id = hotel_id
        self.name = customer_name
        self.last_name = customer_last_name
        self.path = db_path
        self.current_date = datetime.datetime.now()
        self.checkout_date = datetime.datetime.now() + datetime.timedelta(days=stay_time)

    def read_database(self):
        hotels_data = pd.read_csv(self.path, dtype={
            'id': 'int',
            'name': 'str',
            'city': 'str',
            'capacity': 'int',
            'available': 'str',
        })
        return hotels_data

    def generate_ticket(self):
        data = self.read_database()
        hotel_name = data.loc[data['id'] == self.hotel_id, 'name'].squeeze()
        hotel_city = data.loc[data['id'] == self.hotel_id, 'city'].squeeze()
        content = f"""
Thank you for booking a room at our hotel.
Your reservation details are as follows:
Hotel ID: {self.hotel_id}
Hotel Name: {hotel_name}
Hotel City: {hotel_city}
Customer Name: {self.name}
Customer Last Name: {self.last_name}
Date of Booking: {self.current_date}
Checkout Date: {self.checkout_date}
        """
        print(content)
        ticket_content = pd.DataFrame({
            'name': [self.name],
            'last_name': [self.last_name],
            'hotel_id': [self.hotel_id],
            'hotel_name': [hotel_name],
            'hotel_city': [hotel_city],
            'date': [self.current_date],
            'checkout_date': [self.checkout_date]
        })
        return ticket_content
