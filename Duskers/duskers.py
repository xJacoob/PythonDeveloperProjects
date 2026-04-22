import argparse
from Game import Game
from Menu import Menu
from Robots import Robots
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("seed", default="random_seed", type=str, nargs='?')
    parser.add_argument("min_time", default=0.0, type=float, nargs='?')
    parser.add_argument("max_time", default=0.0, type=float, nargs='?')
    parser.add_argument("list_of_places",
                        default="Pleasant_Park,Anarchy_Acres,Wailing_Woods,Lonely_Lodge,Retail_Row,Fatal_Fields,Flush_Factory,Loot_Lake,Greasy_Grove",
                        type=str, nargs='?')

    args = parser.parse_args()

    random.seed(args.seed)

    with open("C:/Users/kubak/Documents/Programming/PycharmProjects/Duskers1/Duskers/task/duskers/title", 'r', encoding='utf-8') as file:
        title = file.read()

    list_of_robots = []
    for i in range(3):
        with open(f"C:/Users/kubak/Documents/Programming/PycharmProjects/Duskers1/Duskers/task/duskers/robotv1", 'r', encoding='utf-8') as file:
            ascii_robot = file.read()
            new_robot = Robots(ascii_robot)
            list_of_robots.append(new_robot)


    exploration_places = args.list_of_places.split(",")
    menu = Menu(title)

    while True:
        in_menu = menu.start_menu()
        if in_menu == "start_game":
            game = Game(list_of_robots, exploration_places, args.min_time, args.max_time, menu.name, 0)
            game_result = game.start_game()
            if game_result:
                menu.save_scores(game_result)
        elif in_menu == "load":
            data = menu.load_game()
            if data is not None:
                loaded_robots = []
                for i in range(data['robots']):
                    with open(f"C:/Users/kubak/Documents/Programming/PycharmProjects/Duskers1/Duskers/task/duskers/robotv1", 'r', encoding='utf-8') as file:
                        ascii_robot = file.read()
                        new_robot = Robots(ascii_robot)
                        loaded_robots.append(new_robot)

                game = Game(loaded_robots, exploration_places, args.min_time, args.max_time, data['name'], data['titanium'], data['titanium_upgrade'], data['probability_upgrade'])
                game_result = game.start_game()
                if game_result:
                    menu.save_scores(game_result)

if __name__ == "__main__":
    main()

