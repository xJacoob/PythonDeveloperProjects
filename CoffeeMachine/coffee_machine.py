# Write your code here
class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.actual_state = "Choosing action"

    def remaining(self):
        return (f"The coffee machine has:\n{self.water} ml of water\n{self.milk} ml of milk\n{self.beans} g of coffee beans\n{self.cups} disposable cups"
          f"\n${self.money} of money\n")

    def buy_action(self, choice):
        if choice == '1':
            if self.water < 250:
                return "Sorry, not enough water!"
            elif self.beans < 16:
                return "Sorry, not enough coffee beans!"
            elif self.cups < 1:
                return "Sorry, not enough disposable cups!"
            else:
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
                return "I have enough resources, making you a coffee!"
        elif choice == '2':
            if self.water < 350:
                return "Sorry, not enough water!"
            elif self.milk < 75:
                return "Sorry, not enough milk!"
            elif self.beans < 20:
                return "Sorry, not enough coffee beans!"
            elif self.cups < 1:
                return "Sorry, not enough disposable cups!"
            else:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
                return "I have enough resources, making you a coffee!"
        elif choice == '3':
            if self.water < 200:
                return "Sorry, not enough water!"
            elif self.milk < 100:
                return "Sorry, not enough milk!"
            elif self.beans < 12:
                return "Sorry, not enough coffee beans!"
            elif self.cups < 1:
                return "Sorry, not enough disposable cups!"
            else:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
                return "I have enough resources, making you a coffee!"
        elif choice == "back":
            return None
        return None

    def fill_water(self, add_water):
        self.water += int(add_water)
        return self.water

    def fill_milk(self, add_milk):
        self.milk += int(add_milk)
        return self.milk

    def fill_beans(self, add_beans):
        self.beans += int(add_beans)
        return self.beans

    def fill_cups(self, cups):
        self.cups += int(cups)
        return self.cups

    def take_action(self):
        earn_money = self.money
        self.money = 0
        return f"I gave you ${earn_money}"


    def process_input(self, input_str):
        if self.actual_state == "Choosing action":
            if input_str == "buy":
                self.actual_state = "Buy"
                return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
            elif input_str == "take":
                return self.take_action()
            elif input_str == "remaining":
                return self.remaining()
            elif input_str == "fill":
                self.actual_state = "Fill water"
                return "Write how many ml of water you want to add:"
        elif self.actual_state == "Fill water":
            self.fill_water(input_str)
            self.actual_state = "Fill milk"
            return "Write how many ml of milk you want to add:"
        elif self.actual_state == "Fill milk":
            self.fill_milk(input_str)
            self.actual_state = "Fill beans"
            return "Write how many coffee beans you want to add:"
        elif self.actual_state == "Fill beans":
            self.fill_beans(input_str)
            self.actual_state = "Fill cups"
            return "Write how many disposable cups you want to add:"
        elif self.actual_state == "Fill cups":
            self.fill_cups(input_str)
            self.actual_state = "Choosing action"
        elif self.actual_state == "Buy":
            self.actual_state = "Choosing action"
            return self.buy_action(input_str)
        return None


if __name__ == "__main__":
    machine = CoffeeMachine()
    while True:
        user_input = input("Write action (buy, fill, take, remaining, exit):")
        if user_input == "exit":
            break
        response = machine.process_input(user_input)
        if response:
            print(response)