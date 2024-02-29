from classess import Hotel, ReservationTicket, CreditCard, CreditCardSecurity, SpaTicket
import os
import random


def main():
    user_hotel_id = 373
    path = 'data/hotels.csv'
    ticket_path = 'data/ticket.csv'
    card_path = 'data/cards.csv'
    card_sec_path = 'data/card_security.csv'

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
            book_hotel_process(hotel_instance, reservation_instance,
                               ticket_path, card_path, card_sec_path, name, last_name)
        else:
            print("No booking made.")

        do_you_want_spa = input(
            "Do you want to book a SPA reservation? (yes/no): ").lower()
        if do_you_want_spa == 'yes':
            spa_reservation_process(
                path, hotel_instance, ticket_path, name, last_name)
        else:
            print("No SPA booking made.")
    else:
        print("Hotel is not available.")


def book_hotel_process(hotel_instance, reservation_instance, ticket_path, card_path, card_sec_path, name, last_name):
    credit_card = '7213876543217213'
    credit_cvc = '473'
    credit_date = "12/29"
    credit_pass = "z9m1vq"

    if authorize_credit_card(card_sec_path, credit_card, credit_pass):
        if validate_and_book_hotel(hotel_instance, reservation_instance, ticket_path, card_path, name, last_name, credit_card, credit_cvc, credit_date):
            print(f"Reservation ticket saved to {ticket_path}")
        else:
            print("There was an error with your credit card.")
    else:
        print("Authorization failed.")


def authorize_credit_card(card_sec_path, credit_card, credit_pass):
    credit_card_security_instance = CreditCardSecurity(
        database_path=card_sec_path, credit_card=credit_card, credit_pass=credit_pass)
    return credit_card_security_instance.authorizing()


def validate_and_book_hotel(hotel_instance, reservation_instance, ticket_path, card_path, name, last_name, credit_card, credit_cvc, credit_date):
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
            return True
        else:
            reservation_content.to_csv(ticket_path, index=False)
            return True
    else:
        return False


def spa_reservation_process(path, hotel_instance, ticket_path, customer_name, customer_last_name):
    if hotel_instance.is_hotel_available():
        spa_ticket = SpaTicket(path, hotel_instance.hotel_id,
                               customer_name, customer_last_name)
        spa_reservation_content = spa_ticket.generate()

        if os.path.exists(ticket_path):
            with open(f'data/ticket/spa_ticket_{random.randint(1, 10000)}.txt', 'a') as file:
                file.write('\n')
                file.write(spa_reservation_content)
                print(spa_reservation_content)
        else:
            with open(f'data/ticket/spa_ticket_{random.randint(1, 10000)}.txt', 'w') as file:
                file.write(spa_reservation_content)
                print(spa_reservation_content)
            print(
                f"SPA reservation ticket saved to 'data/spa_ticket_{random.randint(1, 10000)}.txt'.")
    else:
        print("Hotel is not available for SPA booking.")


if __name__ == '__main__':
    while True:
        main()
        do_you_want_to_continue = input("Do you want to continue? (yes/no): ").lower()
        if do_you_want_to_continue == 'no':
            break
        else:
            continue
