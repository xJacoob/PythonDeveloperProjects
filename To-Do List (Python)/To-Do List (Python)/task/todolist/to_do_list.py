class ToDoList:
    def __init__(self):
        self.todo_list = ["Do yoga", "Make a breakfast", "Learn the basics of SQL", "Learn about ORM"]

    def print_todo_list(self):
        print("Today:")
        for i, item in enumerate(self.todo_list):
            print(f"{i + 1}) {item}")