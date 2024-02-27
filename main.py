from utility import Hotel, ReservationTicket, UserInfo

if __name__ == '__main__':
    # user_hotel_id = int(input("Enter a hotel ID: "))
    user_hotel_id = 449
    path = 'hotels.csv'
    hotel_instance = Hotel(db_path=path, hotel_id=user_hotel_id)
    hotel_instance.check_and_update_availability()
    user_instance = UserInfo()
    print(hotel_instance.read_db())
    if hotel_instance.is_hotel_available():
        # customer_name = input("Enter your name: ")
        # customer_last_name = input("Enter your last name: ")
        customer_name = 'John'
        customer_last_name = 'Doe'
        reservation_instance = ReservationTicket(
            user_hotel_id, customer_name, customer_last_name, path)
        reservation_instance.generate_ticket()
        print("Hotel is available.")
        do_you_want_to_book = input(
            "Do you want to book this hotel? (yes/no): ")
        if do_you_want_to_book == 'yes':
            hotel_instance.book_hotel()
    else:
        print("Hotel is not available.")
