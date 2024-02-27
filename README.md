# GitHub Scraping Program Hotel Booking

This is a Python program that uses web scraping techniques to extract data from GitHub repositories. The program retrieves information such as repository name, description, stars, forks, and contributors.

This program contains 3 classes:

- UserInfo - stores user information like name, email, phone number
- Hotel - stores hotel information like name, address, rooms
- ReservationTicket - stores reservation details like user, hotel, check-in/out dates

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.x
- pandas

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/EMPChief/Python-Hotel-Booking
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   ```

3. Start the virtual environment:

   - Windows:
     ```shell
     venv\Scripts\activate
     ```
   - Linux:
     ```shell
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```shell
   pip install beautifulsoup4
   pip install requests
   ```

## Usage

1. Open the `main.py` file.

2. Modify the following variables according to your needs:

   ```python
   repository_url = "https://github.com/EMPChief/Python-Hotel-Booking"
   ```

3. Run the program:

   ```shell
   python main.py
   ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
