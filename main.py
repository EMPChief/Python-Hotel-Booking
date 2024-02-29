from utility import Hotel, ReservationTicket, CreditCard
import pandas as pd
import os
import re

if __name__ == '__main__':
    user_hotel_id = 373
    path = 'hotels.csv'
    ticket_path = 'ticket.csv'
    card_path = 'cards.csv'

    hotel_instance = Hotel(database_path=path, hotel_room_id=user_hotel_id)
    hotel_instance.check_and_update_availability()

    print(hotel_instance.read_database())

    if hotel_instance.is_hotel_available():
        name = 'John'
        last_name = 'Doe'
        stay_time = 5

        reservation_instance = ReservationTicket(
            user_hotel_id, name, last_name, stay_time, db_path=path)

        print("Hotel is available.")
        do_you_want_to_book = input(
            "Do you want to book this hotel? (yes/no): ").lower()

        if do_you_want_to_book == 'yes':
            credit_card = '1234567812347213'
            credit_cvc = '473'
            credit_date = "12/29"

            credit_card_instance = CreditCard(
                name, last_name, card_path,
                credit_card=credit_card,
                credit_cvc=credit_cvc,
                credit_date=credit_date
            )

            if credit_card_instance.validate():
                hotel_instance.book_hotel()
                reservation_content = reservation_instance.generate_ticket()

                if os.path.exists(ticket_path):
                    reservation_content.to_csv(
                        ticket_path, mode='a', header=False, index=False)
                    print(f"Reservation ticket saved to {ticket_path}")
                else:
                    reservation_content.to_csv(ticket_path, index=False)
            else:
                print("There was an error with your credit card.")
        else:
            print("No booking made.")
    else:
        print("Hotel is not available.")
