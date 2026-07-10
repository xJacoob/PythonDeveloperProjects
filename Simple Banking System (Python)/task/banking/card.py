import random

class Card:
    
    card_prefix = '400000'
    
    def __init__(self, account_number):
        self.checksum = random.randint(0, 9)
        self.card_number = self.card_prefix + account_number + str(self.checksum)
        self.pin = ''.join(str(random.randint(0, 9)) for _ in range(4))
        self.account_number = account_number
        self.balance = 0

    def __str__(self):
        return f"Your card number:\n{self.card_number}\nYour card PIN:\n{self.pin}"