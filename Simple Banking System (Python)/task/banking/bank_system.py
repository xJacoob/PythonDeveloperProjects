from card import Card
import random

class BankSystem:
    def __init__(self):
        self.card_list = []

    @staticmethod
    def generate_account_number() -> str:
        account_number = [random.randint(0, 9) for _ in range(9)]
        formated_account_number = ''.join(map(str, account_number))
        return formated_account_number

    def check_if_unique(self) -> str:
        existing_account_numbers = {card.account_number for card in self.card_list}
        account_number = self.generate_account_number()

        while account_number in existing_account_numbers:
            account_number = self.generate_account_number()

        return account_number

    def log_into_account(self, user_card_number, user_pin) -> tuple:
        for card in self.card_list:
            if user_card_number == card.card_number and user_pin == card.pin:
                return True, card
        else:
            return False, None

    def menu(self):
        while True:
            print("1. Create an account\n2. Log into account\n0. Exit")
            user_input = input('>')
            if user_input == '1':
                account_number = self.check_if_unique()
                card = Card(account_number)
                self.card_list.append(card)
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
                            print(f"Balance: {account.balance}\n")
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

