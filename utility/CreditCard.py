import pandas as pd
import datetime

class CreditCard:
    def __init__(self, name=None, last_name=None, card_path=None, credit_card=None, credit_cvc=None, credit_date=None):
        self.name = name
        self.last_name = last_name
        self.path = card_path
        self.credit_card = credit_card
        self.credit_cvc = credit_cvc
        self.credit_date = credit_date
        
    def read_database(self):
        cards_data = pd.read_csv(self.path, dtype={
            'number': 'str',
            'expiration': 'str',
            'cvc': 'str',
            'holder': 'str',
        })
        return cards_data
        
    def validate(self):
        cards_data = self.read_database()
        current_date = datetime.datetime.now().date()

        card_info = cards_data[cards_data['number'].str[-4:] == str(self.credit_card)[-4:]]
        if card_info.empty:
            return False

        card_exp = card_info['expiration'].iloc[0]
        card_cvc = card_info['cvc'].iloc[0] if 'cvc' in card_info.columns else None
        card_holder = card_info['holder'].iloc[0]

        card_exp_date = datetime.datetime.strptime(card_exp, '%m/%y').date()

        if card_exp_date > current_date and \
        card_cvc == str(self.credit_cvc) and \
        card_holder.lower() == f"{self.name.lower()} {self.last_name.lower()}":
            return True
        else:
            return False
