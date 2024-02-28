from utility import Hotel, ReservationTicket, UserInfo
import pandas as pd
import os

if __name__ == '__main__':
    # user_hotel_id = int(input("Enter a hotel ID: "))
    user_hotel_id = 812
    path = 'hotels.csv'
    ticket_path = 'ticket.csv'
    hotel_instance = Hotel(database_path=path, hotel_room_id=user_hotel_id)
    hotel_instance.check_and_update_availability()
    user_instance = UserInfo()
    print(hotel_instance.read_database())  # Corrected method name
    if hotel_instance.is_hotel_available():
        # name = input("Enter your name: ")
        # last_name = input("Enter your last name: ")
        # stay_time = int(input("Enter the number of days you want to stay: "))
        name = 'John'
        last_name = 'Doe'
        stay_time = 2
        reservation_instance = ReservationTicket(
            user_hotel_id, name, last_name, stay_time, db_path=path)
        print("Hotel is available.")
        do_you_want_to_book = input(
            "Do you want to book this hotel? (yes/no): ").lower()
        if do_you_want_to_book == 'yes':
            hotel_instance.book_hotel()
            reservation_content = reservation_instance.generate_ticket()
            # Check if file exists, if yes then append, else create new
            if os.path.exists(ticket_path):
                reservation_content.to_csv(
                    ticket_path, mode='a', header=False, index=False)
                print("Reservation ticket saved to {ticket_path}")
                print("Path did not exist, created a new one.")
            else:
                reservation_content.to_csv(ticket_path, index=False)
            print(f"Reservation ticket saved to {ticket_path}")
    else:
        print("Hotel is not available.")
