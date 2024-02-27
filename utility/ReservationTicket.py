import pandas as pd

class ReservationTicket:
    def __init__(self, hotel_id, name, last_name, db_path=None):
        self.hotel_id = hotel_id
        self.name = name
        self.last_name = last_name
        self.path = db_path

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
        pass
