import os

class ManageCommands:

    def main_logic(self):
        print("Input the command")

        while True:
            input_from_user = input(">")
            if input_from_user == "pwd":
                path = self.get_path()
                print(path)
            elif input_from_user == "cd ..":
                last_directory = self.move_up()
                print(last_directory)
            elif input_from_user.startswith("cd "):
                input_from_user = input_from_user[3:]
                try:
                    last_directory = self.move_to_relative_path(input_from_user)
                    print(last_directory)
                except FileNotFoundError:
                    print("File Not Found")
            elif input_from_user == "quit":
                break
            else:
                print("Invalid Command")

    def get_path(self):
        path = os.getcwd()
        return path

    def get_last_directory(self):
        path = self.get_path()
        last_directory = os.path.basename(path)
        return last_directory

    def move_up(self):
        os.chdir("..")
        last_directory = self.get_last_directory()
        return last_directory

    def move_to_relative_path(self, relative_path):
        os.chdir(relative_path)
        last_directory = self.get_last_directory()
        return last_directory
