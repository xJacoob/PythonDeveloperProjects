import random

class Card:
    
    card_prefix = '400000'
    
    def __init__(self, account_number):
        self.account_number = account_number
        self.checksum = Card.luhn_algorithm(self.card_prefix + self.account_number)
        self.card_number = self.card_prefix + account_number + str(self.checksum)
        self.pin = ''.join(str(random.randint(0, 9)) for _ in range(4))
        self.balance = 0

    @staticmethod
    def luhn_algorithm(digits: str) -> int:
        number_list = [int(x) for x in digits]
        for i in range(len(number_list)):
            if (i + 1) % 2 != 0:
                number_list[i] = int(number_list[i]) * 2

            if number_list[i] > 9:
                number_list[i] -= 9

        sum_number = sum(number_list)
        check_sum = (10 - (sum_number % 10)) % 10
        return check_sum

    def __str__(self):
        return f"Your card number:\n{self.card_number}\nYour card PIN:\n{self.pin}"