from datetime import date, datetime, timedelta
from models import Task, Session

class Menu:
    def __init__(self):
        self.session = Session()

    def main_logic(self):
        while True:
            answer = Menu.menu()
            if answer == "today":
                self.show_today_tasks()
            elif answer == "week":
                self.show_weekly_tasks()
            elif answer == "all":
                self.all_tasks()
            elif answer == "missed":
                self.missed_tasks()
            elif answer == "add":
                self.add_task()
            elif answer == "delete":
                self.delete_task()
            elif answer == "exit":
                print("\nBye!")
                exit()

    @staticmethod
    def menu():
        user_input = input("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add a task\n6) Delete a task\n0) Exit\n> ")
        if user_input == "1":
            return "today"
        elif user_input == "2":
            return "week"
        elif user_input == "3":
            return "all"
        elif user_input == "4":
            return "missed"
        elif user_input == "5":
            return "add"
        elif user_input == "6":
            return "delete"
        elif user_input == "0":
            return "exit"

        return None

    def add_task(self):
        user_task = input("\nEnter a task\n> ")
        while True:
            user_deadline = input("Enter a deadline\n> ")
            try:
                database_format = datetime.strptime(user_deadline, "%Y-%m-%d").date()
                new_row = Task(task=user_task, deadline=database_format)
                break
            except ValueError:
                print("\nInvalid date!\n")
        self.session.add(new_row)
        self.session.commit()
        print("The task has been added!\n")

    def show_today_tasks(self):
        all_tasks = self.session.query(Task).all()
        today = date.today()
        todays_tasks = [task for task in all_tasks if task.deadline == today]

        print(f"\nToday {today.strftime('%d %b')}:")
        if not todays_tasks:
            print("Nothing to do!\n")
        else:
            for index, task in enumerate(todays_tasks):
                print(f"{index + 1}. {task.task}")
            print("")

    def show_weekly_tasks(self):
        today = date.today()
        week = today + timedelta(days=6)
        week_tasks = self.session.query(Task).filter(Task.deadline.between(today, week)).all()

        for i in range(7):
            current_day = today + timedelta(days=i)
            print(f"{current_day.strftime('%A %d %b')}:")
            day_tasks = [task for task in week_tasks if task.deadline == current_day]

            if day_tasks:
                for index, task in enumerate(day_tasks):
                    print(f"{index + 1}. {task.task}")
                print("")
            else:
                print("Nothing to do!\n")

    def all_tasks(self):
        all_tasks = self.session.query(Task).order_by(Task.deadline.asc()).all()
        if not all_tasks:
            print("Nothing to do!\n")
        else:
            for index, task in enumerate(all_tasks):
                print(f"{index + 1}. {task.task}. {task.deadline.day} {task.deadline.strftime('%b')}")
            print("")

    def missed_tasks(self):
        missed_tasks = self.session.query(Task).filter(Task.deadline < date.today()).all()

        print(f"\nMissed tasks:")
        if not missed_tasks:
            print("All tasks have been completed\n")
        else:
            for index, task in enumerate(missed_tasks):
                print(f"{index + 1}. {task.task}. {task.deadline.day} {task.deadline.strftime('%b')}")
            print("")

    def delete_task(self):
        all_tasks = self.session.query(Task).order_by(Task.deadline.asc()).all()
        print("\nChoose the number of the task you want to delete:")
        if not all_tasks:
            print("Nothing to delete\n")
        else:
            for index, task in enumerate(all_tasks):
                print(f"{index + 1}. {task.task}. {task.deadline.day} {task.deadline.strftime('%b')}")
            user_input = input("> ")
            task = all_tasks[int(user_input) - 1]
            self.session.delete(task)
            self.session.commit()
            print("The task has been deleted!\n")