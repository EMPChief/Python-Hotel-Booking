import pandas as pd


class Hotel:
    def __init__(self, database_path=None, hotel_id=None):
        self.path = database_path
        self.hotel_id = hotel_id

    def read_database(self):
        hotels_data = pd.read_csv(self.path, dtype={
            'id': 'int',
            'name': 'str',
            'city': 'str',
            'capacity': 'int',
            'available': 'str',
        })
        return hotels_data

    def check_and_update_availability(self):
        hotels_data = self.read_database()
        for index, row in hotels_data.iterrows():
            if row['capacity'] > 0 and row['available'] == 'no':
                hotels_data.loc[index, 'available'] = 'yes'
            if row['capacity'] == 0 and row['available'] == 'yes':
                hotels_data.loc[index, 'available'] = 'no'
        hotels_data.to_csv(self.path, index=False)
        print("Availability checked and updated.")

    def book_hotel(self):
        hotels_data = self.read_database()
        capacity = hotels_data.loc[hotels_data['id']
                                   == self.hotel_id, 'capacity'].values[0]
        availability = hotels_data.loc[hotels_data['id']
                                       == self.hotel_id, 'available'].values[0]

        if availability == 'yes' and capacity > 0:
            hotels_data.loc[hotels_data['id'] == self.hotel_id, 'capacity'] -= 1

            if hotels_data.loc[hotels_data['id'] == self.hotel_id, 'capacity'].values[0] == 0:
                hotels_data.loc[hotels_data['id'] ==
                                 self.hotel_id, 'available'] = 'no'

            hotels_data.to_csv(self.path, index=False)
            print("Room has been booked.")
        elif availability == 'no':
            print("Room is already booked.")
        else:
            print("No more capacity available.")

    def is_hotel_available(self):
        hotels_data = self.read_database()
        availability = hotels_data.loc[hotels_data['id']
                                       == self.hotel_id, 'available'].values[0]
        return availability == 'yes'
