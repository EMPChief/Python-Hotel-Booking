

class ReservationTicket:
    def __init__(self, hotel_id, name, last_name, db_path=None):
        self.hotel_id = hotel_id
        self.name = name
        self.last_name = last_name
        self.path = db_path
    
    def generate_ticket(self):
        pass