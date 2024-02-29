import pandas as pd

class CreditCard:
    def __init__(self, first_name=None, last_name=None, card_path=None, credit_card=None, credit_cvc=None, credit_date=None):
        self.first_name = first_name
        self.last_name = last_name
        self.path = card_path
        self.credit_card = credit_card
        self.credit_cvc = credit_cvc
        self.credit_date = credit_date

    def read_database(self):
        try:
            cards_data = pd.read_csv(self.path, dtype={
                'number': 'str',
                'expiration': 'str',
                'cvc': 'str',
                'holder': 'str',
            })
            return cards_data
        except Exception as e:
            print(f"Error reading database: {e}")
            return None

    def validate(self):
        try:
            card_data = self.read_database()
            if card_data is None:
                return False

            provided_last_4 = self.credit_card[-4:]
            matched_card = card_data[card_data['number'].str[-4:] == provided_last_4]

            if not matched_card.empty and matched_card['cvc'].iloc[0] == self.credit_cvc and matched_card['expiration'].iloc[0] == self.credit_date:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error validating card: {e}")
            return False
