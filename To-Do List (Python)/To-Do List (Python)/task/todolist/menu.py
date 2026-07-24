from datetime import date
from models import Task, Session

class Menu:
    def __init__(self):
        self.session = Session()

    def main_logic(self):
        while True:
            answer = Menu.menu()
            if answer == "show":
                self.show_today_tasks()
            elif answer == "add":
                self.add_task()
            elif answer == "exit":
                print("\nBye!")
                exit()

    @staticmethod
    def menu():
        user_input = input("1) Today's tasks\n2) Add a task\n0) Exit\n> ")
        if user_input == "1":
            return "show"
        elif user_input == "2":
            return "add"
        elif user_input == "0":
            return "exit"

        return None

    def add_task(self):
        user_task = input("\nEnter a task\n> ")
        new_row = Task(task=user_task)
        self.session.add(new_row)
        self.session.commit()
        print("The task has been added!\n")

    def show_today_tasks(self):
        all_tasks = self.session.query(Task).all()
        todays_tasks = [task for task in all_tasks if task.deadline == date.today()]

        print("\nToday:")
        if not todays_tasks:
            print("Nothing to do!\n")

        for index, task in enumerate(todays_tasks):
            print(f"{index + 1}. {task.task}")