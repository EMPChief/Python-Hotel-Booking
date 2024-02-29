import pandas as pd
from .CreditCard import CreditCard

class CreditCardSecurity(CreditCard):
    def __init__(self, database_path=None, credit_card=None, credit_pass=None):
        super().__init__(credit_card=credit_card)
        self.path = database_path
        self.credit_pass = credit_pass
    
    def read_database(self):
        try:
            cards_data = pd.read_csv(self.path, dtype={
                'number': 'int',
                'password': 'str',
            })
            return cards_data
        except Exception as e:
            print(f"Error reading database: {e}")
            return None
        
    def authorizing(self):
        try:
            data_verf = self.read_database()
            matched_card = data_verf[data_verf['number'] == int(self.credit_card)]
            if matched_card.empty:
                print("Credit card not found.")
                return False
            password = matched_card['password'].iloc[0]
            if password == self.credit_pass:
                return True
            else:
                print("Incorrect password.")
                return False
        except Exception as e:
            print(f"Error authorizing: {e}")
            return False
