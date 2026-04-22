import os
import time
import random
import datetime
import json
from Robots import Robots

class Game:
    def __init__(self, robot_list, list_of_places, min_time, max_time, name, titan, titanium_scan=False, probability_scan=False):
        self.list_of_robots = robot_list
        self.list_of_places = list_of_places
        self.min_time = min_time
        self.max_time = max_time
        self.name = name
        self.titanium = titan
        self.scan_titanium_flag = titanium_scan
        self.scan_probability_flag = probability_scan

    def start_game(self):
        while True:
            self.robot_screen()
            choice = self.game_menu()
            if choice == "explore":
                end_game = self.explore()
                if end_game == "game_over":
                    return {'name': self.name, "score": self.titanium}
            elif choice == "upgrade":
                self.upgrade_store()
            elif choice == "save":
                self.save_game()
            elif choice == "menu":
                self.menu_screen()
                while True:
                    choice = self.pause_menu()
                    if choice == "back":
                        self.robot_screen()
                        break
                    elif choice == "main":
                        return
                    elif choice == "save":
                        self.save_game()
                    elif choice == "exit":
                        exit()
                if choice == "main":
                    break

    def game_menu(self):
        choice = input("Your command:").lower()
        if choice == "ex":
            return "explore"
        elif choice == "up":
            return "upgrade"
        elif choice == "save":
            return "save"
        elif choice == "m":
            return "menu"
        else:
            print("Invalid input\n")
            return None

    def pause_menu(self):
        choice = input("Your command:").lower()
        if choice == "back":
            return "back"
        elif choice == "main":
            return "main"
        elif choice == "save":
            return "save"
        elif choice == "exit":
            print("Coming SOON! Thanks for playing!")
            return "exit"
        else:
            print("Invalid input\n")
            return None

    def pseudo_time(self):
        epoch_time = int(time.time())
        diff_time = int(self.max_time - self.min_time)
        pseudo_time = (epoch_time % (diff_time + 1) + self.min_time)
        return int(pseudo_time)

    def time_animation(self):
        pseudo_time = self.pseudo_time()
        print("Searching", end="", flush=True)
        for i in range(pseudo_time):
            time.sleep(1)
            print(".", end="", flush=True)

    def value_of_titanium(self):
        while True:
            titanium = random.randint(10, 100)
            yield titanium

    def place_probability(self):
        while True:
            probablity = random.random()
            yield probablity

    def places(self):
        explored_places = {}
        max_location_to_explore = random.randint(1, 9)
        gen_titanium = self.value_of_titanium()
        gen_probability = self.place_probability()


        for i in range(max_location_to_explore):
            random_place = random.choice(self.list_of_places)
            explored_places[i + 1] = (random_place, next(gen_titanium), next(gen_probability))
            yield explored_places

    def explore(self):
        gen_places = self.places()
        current_list_of_places = next(gen_places)
        self.time_animation()
        no_more_locations = False

        while True:
            print()
            for key, value in current_list_of_places.items():
                display_text = f"[{key}] {value[0].replace("_", " ")}"

                if self.scan_titanium_flag:
                    display_text += f" Titanium: {value[1]}"

                if self.scan_probability_flag:
                    display_text += f" Encounter rate: {round(value[2] * 100)}%"

                print(display_text)

            if not no_more_locations:
                print("\n[S] to continue searching")
            else:
                print("\nNothing more in sight\n[BACK].")

            print("[Back] to return HUB")
            user_input = input("Your command:")

            if user_input == 'back':
                break

            elif user_input == 's':
                if no_more_locations:
                    print("Nothing more in sight\n[BACK].")
                    continue
                try:
                    self.time_animation()
                    current_list_of_places = next(gen_places)
                except StopIteration:
                    no_more_locations = True
                    print("Nothing more in sight.\n[BACK]")

            elif user_input.isdigit():
                choice = int(user_input)
                if choice in current_list_of_places:
                    chances = random.random()

                    if current_list_of_places[int(user_input)][2] <= chances:
                        self.titanium += current_list_of_places[int(user_input)][1]
                        print(f"Deploying robots\n{current_list_of_places[int(user_input)][0].replace("_", " ")} explored successfully, "
                            f"with no damage taken.\nAcquired {current_list_of_places[int(user_input)][1]} lumps of titanium")

                    elif current_list_of_places[int(user_input)][2] > chances:
                        self.list_of_robots.pop()
                        if self.list_of_robots:
                            self.titanium += current_list_of_places[int(user_input)][1]
                            print(
                            f"Deploying robots\n{current_list_of_places[int(user_input)][0].replace("_", " ")}\nEnemy encounter!!!\nexplored successfully, "
                            f"1 robot lost..\nAcquired {current_list_of_places[int(user_input)][1]} lumps of titanium")

                        else:
                            print(
                                f"Deploying robots\n{current_list_of_places[int(user_input)][0].replace("_", " ")}\nEnemy encounter!!!\nMission aborted, "
                                f"the last robot lost..\n")
                            print("""
                                |==============================|
                                |          GAME OVER!          |
                                |==============================|""")
                            return "game_over"

                    break

                else:
                    print("Invalid input\n")
            else:
                print("Invalid input\n")

    def save_game(self):
        date = datetime.datetime.now()
        formated_date = date.strftime("%Y-%m-%d %H:%M")
        dict = {
            'name': self.name,
            'titanium': self.titanium,
            'robots': len(self.list_of_robots),
            'date': formated_date,
            'titanium_upgrade': self.scan_titanium_flag,
            'probability_upgrade': self.scan_probability_flag
        }
        print("Select save slot:")
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
            with open(f"{file_name}", 'w') as f:
                json.dump(dict, f)
                print("""
                        |==============================|
                        |    GAME SAVED SUCCESSFULLY   |
                        |==============================|""")
        else:
            print("Invalid input\n")


    def menu_screen(self):
        print("""
                              |==========================|
                              |            MENU          |
                              |                          |
                              | [Back] to game           |
                              | Return to [Main] Menu    |
                              | [Save] and exit          |
                              | [Exit] game              |
                              |==========================|""")

    def robot_screen(self):
        print(
            "+=============================================================================================================================+")

        if self.list_of_robots:

            robot_lines = [str(robot).splitlines() for robot in self.list_of_robots]

            for line in zip(*robot_lines):
                print(" | ".join(line))

        print(f"""
+=============================================================================================================================+
| Titanium: {self.titanium}                                                                                                   |
|                                                                                                                             |
+=============================================================================================================================+
|                                        [Ex]plore                               [Up]grade                                    |
|                                        [Save]                                  [M]enu                                       |
+=============================================================================================================================+""")

    def upgrade_store(self):
        print("""
                       |================================|
                       |          UPGRADE STORE         |
                       |                         Price  |
                       | [1] Titanium Scan         250  |
                       | [2] Enemy Encounter Scan  500  |
                       | [3] New Robot            1000  |
                       |                                |
                       | [Back]                         |
                       |================================|""")

        user_input = input("Your command:\n")

        if user_input == "1":
            if self.titanium >= 250:
                self.titanium -= 250
                self.scan_titanium_flag = True
                print("Purchase successful. You can now see how much titanium you can get from each found location.")
            else:
                print("Not enough titanium!\n")

        elif user_input == "2":
            if self.titanium >= 500:
                self.titanium -= 500
                self.scan_probability_flag = True
                print("Purchase successful. You will now see how likely you will encounter an enemy at each found location.")
            else:
                print("Not enough titanium\n")

        elif user_input == "3":
            if self.titanium >= 1000:
                self.titanium -= 1000
                with open(f"C:/Users/kubak/Documents/Programming/PycharmProjects/Duskers1/Duskers/task/duskers/robotv1",
                    'r', encoding='utf-8') as file:
                    ascii_robot = file.read()
                    new_robot = Robots(ascii_robot)
                    self.list_of_robots.append(new_robot)
                    print("Purchase successful. You now have an additional robot")
            else:
                print("Not enough titanium\n")

        elif user_input == "back":
            return
        else:
            print("Invalid input\n")
