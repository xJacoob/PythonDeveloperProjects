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

    def add_income(self, user_card_number, amount):
        self.db.increase_balance(user_card_number, amount)

    def delete_account(self, user_card_number):
        self.db.delete_by_number(user_card_number)

    def is_valid_number_to_transfer(self, number, other_number):
        other_number_without_check_sum = other_number[: -1]
        luhn_algorithm = Card.luhn_algorithm(other_number_without_check_sum)

        if luhn_algorithm != int(other_number[-1]):
            print("Probably you made a mistake in the card number. Please try again!")
            return False

        other_account = self.db.find_by_number(other_number)
        if other_account is None:
            print("Such a card does not exist.")
            return False

        if number == other_number:
            print("You can't transfer money to the same account!")
            return False

        return True

    def do_transfer(self, number, other_number, amount):
        account = self.db.find_by_number(number)
        if account['balance'] < int(amount):
            print("Not enough money!")
            return

        self.db.decrease_balance(number, int(amount))
        self.db.increase_balance(other_number, int(amount))
        print("Success!")

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
                        elif choice == 'income':
                            user_income = input("Enter income:\n>")
                            self.add_income(user_card_number, int(user_income))
                            account = self.db.find_by_number(user_card_number)
                            print(f"Income was added!")
                        elif choice == 'transfer':
                            other_number = input("Enter card number:\n>")
                            if self.is_valid_number_to_transfer(user_card_number, other_number):
                                user_amount = input("Enter how much money you want to transfer:\n>")
                                self.do_transfer(user_card_number, other_number, user_amount)
                                account = self.db.find_by_number(user_card_number)
                        elif choice == 'close':
                            self.delete_account(user_card_number)
                            print("The account has been closed!")
                            break
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
            print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
            user_input = input('>')
            if user_input == '1':
                return 'balance'
            elif user_input == '2':
                return 'income'
            elif user_input == '3':
                return 'transfer'
            elif user_input == '4':
                return 'close'
            elif user_input == '5':
                return 'logout'
            elif user_input == '0':
                return 'exit'

