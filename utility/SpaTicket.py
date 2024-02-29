import pandas as pd

class SpaTicket:
    def __init__(self, path, hotel_id, customer_name, customer_last_name):
        self.hotel_id = hotel_id
        self.customer_name = customer_name
        self.customer_last_name = customer_last_name
        self.path = path

    def read_database(self):
        hotels_data = pd.read_csv(self.path, dtype={
            'id': 'int',
            'name': 'str',
            'city': 'str',
            'capacity': 'int',
            'available': 'str',
        })
        return hotels_data

    def generate(self):
        hotels_data = self.read_database()
        hotel_name = hotels_data.loc[hotels_data['id'] == self.hotel_id, 'name'].values[0]
        content = f"""
        Thank you for your SPA reservation!
        Here are your SPA booking details:
        Name: {self.customer_name} {self.customer_last_name}
        Hotel Name: {hotel_name}
        """
        return content
