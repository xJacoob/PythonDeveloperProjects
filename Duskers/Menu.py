import os
import json
from Game import Game

class Menu:
    def __init__(self, title_screen):
        self.title_screen = title_screen
        self.name = ""

    def start_menu(self):
        while True:
            print(self.screen_title())

            while True:
                choice = self.main_menu()
                if choice == "load":
                    return "load"
                elif choice == "high":
                    self.display_scores()
                    break
                elif choice == "new":
                    self.name = self.nickname()
                    again_flag = False
                    while True:
                        choice = self.commands(again_flag)
                        if choice == "yes":
                            return "start_game"
                        elif choice == "no":
                            again_flag = True
                            continue
                        elif choice == "menu":
                            break

                if choice == "menu":
                    break
                elif choice == "yes":
                    break
                elif choice == "high":
                    continue
                elif choice == "help":
                    self.help_instructions()
                    break
                elif choice == "exit":
                    exit()


    def main_menu(self):
        user_input = input("Your command:").lower()
        if user_input == "new":
            return "new"
        elif user_input == "load":
            return "load"
        elif user_input == "exit":
            print("Thanks for playing, bye!")
            return "exit"
        elif user_input == "high":
            return "high"
        elif user_input == "back":
            print(self.screen_title())
            return None
        elif user_input == "help":
            return 'help'
        elif user_input == "main":
            return "main"
        else:
            print("Invalid input")
            return None

    def help_instructions(self):
        print("""
|==============================================================================|
|                                  HELP MENU                                   |
|==============================================================================|
| COMMAND THE FLEET:                                                           |
| You are the commander of a fleet of exploration robots.                      |
| Your goal is to gather as much Titanium as possible from abandoned locations.|
|                                                                              |
| CORE COMMANDS:                                                               |
| [Ex]plore - Send robots to search locations for Titanium.                    |
|             Be careful! Some locations have enemies that destroy robots.     |
| [Up]grade - Spend Titanium to buy scanners or new robots in the store.       |
| [Save]    - Save your current progress to a local file.                      |
| [M]enu    - Open the pause menu to save or exit the game.                    |
|                                                                              |
| GAME OVER:                                                                   |
| The game ends when you lose your last robot. Your Titanium score will then   |
| be saved to the High Scores board. Good luck, Commander!                     |
|==============================================================================|""")
        print("\n[BACK] to return to Main Menu")

        while True:
            user_input = input("Your command:").lower()
            if user_input == "back":
                break
            else:
                print("Invalid input\n")

    def commands(self, again=False):
        if not again:
            print("Are you ready to begin?\n[YES] [NO] Return to Main[Menu]\n")
        else:
            print("How about now.\nAre you ready to begin?\n[YES] [NO]\n")

        user_input = input("Your command:").lower()

        if user_input == "no":
            return "no"
        elif user_input == "yes":
            return "yes"
        elif user_input == "menu":
            return "menu"
        else:
            print("Invalid input\n")
            return None

    def save_scores(self, result):
        scores = []

        if os.path.isfile("high_scores.json"):
            with open("high_scores.json", 'r') as f:
                scores = json.load(f)

        scores.append(result)
        scores.sort(key=lambda x: x['score'], reverse=True)
        scores = scores[:10]

        with open("high_scores.json", 'w') as f:
            json.dump(scores, f)

    def display_scores(self):
        print("HIGH SCORES:")
        scores = []
        if os.path.isfile("high_scores.json"):
            with open("high_scores.json", 'r') as f:
                scores = json.load(f)

        if not scores:
            print("No high scores found.")
        else:
            for i, wynik in enumerate(scores):
                print(f"({i + 1}) {wynik['name']} {wynik['score']}")

        print("\n [BACK]")

        while True:
            user_input = input("Your command:").lower()
            if user_input == "back":
                break
            else:
                print("Invalid input\n")

    def screen_title(self):
        return f"""{self.title_screen}\n[New] Game\n[Load] Game\n[High] Scores\n[Help]\n[Exit]"""

    def nickname(self):
        user_nick = input("Enter your name:")
        print(f"Greetings, commander {user_nick.capitalize()}!")
        return user_nick

    def load_game(self):
        while True:
            for i in range(3):
                file_name = f"save_file{i + 1}.json"
                if os.path.isfile(file_name):
                    with open(file_name, 'r') as f:
                        data = json.load(f)
                    print(f"[{i + 1}] {data['name']} Titanium: {data['titanium']} Robots: {data['robots']} Last save: {data['date']}")
                else:
                    print(f"[{i + 1}] empty")

            user_input = input("Your command:\n")
            if user_input in ["1", "2", "3"]:
                file_name = f"save_file{user_input}.json"
                if os.path.isfile(file_name):
                    with open(f"{file_name}", 'r') as f:
                        data = json.load(f)
                        print(f"""
                        |==============================|
                        |    GAME LOADED SUCCESSFULLY  |
                        |==============================|
                        Welcome back, commander {data['name']}!""")
                        return data
                else:
                    print("Empty slot!")
            elif user_input == "back":
                return None
            else:
                print("Invalid input\n")

    def __str__(self):
        return f"{self.title_screen}"
