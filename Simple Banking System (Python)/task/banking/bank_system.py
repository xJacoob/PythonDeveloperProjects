from card import Card
from data_base import DataBase
import random

class BankSystem:
    def __init__(self):
        self.db = DataBase()

    @staticmethod
    def generate_account_number() -> str:
        account_number = [random.randint(0, 9) for _ in range(9)]
        formated_account_number = ''.join(map(str, account_number))
        return formated_account_number

    def check_if_unique(self) -> str:
        account_number = self.generate_account_number()
        pattern = Card.card_prefix + account_number + '%'
        while self.db.find_by_partial_number(pattern) is not None:
            account_number = self.generate_account_number()
            pattern = Card.card_prefix + account_number + '%'
        return account_number

    def log_into_account(self, user_card_number, user_pin) -> tuple:
        account = self.db.find_by_number_and_pin(user_card_number, user_pin)
        if account is not None:
            return True, account
        return False, None

    def menu(self):
        while True:
            print("1. Create an account\n2. Log into account\n0. Exit")
            user_input = input('>')
            if user_input == '1':
                account_number = self.check_if_unique()
                card = Card(account_number)
                self.db.add_card(card.card_number, card.pin)
                print(f"Your card has been created\n{card}")
            elif user_input == '2':
                print("Enter your card number:")
                user_card_number = input('>')
                print("Enter your PIN:")
                user_pin = input('>')
                is_valid, account = self.log_into_account(user_card_number, user_pin)
                if is_valid:
                    print("You have successfully logged in!")
                    while True:
                        choice = self.in_card_menu()
                        if choice == 'balance':
                            print(f"Balance: {account['balance']}\n")
                        elif choice == 'logout':
                            print("You have successfully logged out!")
                            break
                        elif choice == 'exit':
                            print("Bye!")
                            exit()
                else:
                    print("Wrong card number or PIN!")
            elif user_input == '0':
                print("Bye!")
                exit()

    @staticmethod
    def in_card_menu():
        while True:
            print("1. Balance\n2. Log out\n0. Exit")
            user_input = input('>')
            if user_input == '1':
                return 'balance'
            elif user_input == '2':
                return 'logout'
            elif user_input == '0':
                return 'exit'

