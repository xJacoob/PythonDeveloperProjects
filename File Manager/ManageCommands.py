import os
from collections import defaultdict
import shutil

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

            elif input_from_user == "ls":
                list_of_files = self.files_and_subdirectories()
                self.print_contents(list_of_files)

            elif input_from_user == "ls -l":
                dict_of_all = self.files_and_directories_with_size()
                self.print_contents(dict_of_all)

            elif input_from_user == "ls -lh":
                dict_of_all = self.calculated_size()
                self.print_contents(dict_of_all)

            elif input_from_user.startswith("mkdir"):
                if input_from_user == "mkdir":
                    print("Specify the name of the directory to be made")
                    continue
                input_from_user = input_from_user[6:]
                try:
                    self.creating_directory(input_from_user)
                except FileExistsError:
                    print("The directory already exists")

            elif input_from_user.startswith("mv ."):
                input_from_user = input_from_user.split()
                if len(input_from_user) != 3:
                    print("Specify the current name of the file or directory and the new location and/or name")
                    continue
                extension = input_from_user[1]
                dst = input_from_user[2]
                path = self.get_path()

                files = [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))
                         and item.endswith(extension)]
                if not files:
                    print(f"File extension {extension} not found in this directory")
                    continue

                for file in files:
                    src = file
                    dst_dir = os.path.join(dst, file)

                    if os.path.exists(dst_dir):
                        while True:
                            print(f"{file} already exists in this directory. Replace? (y/n)")
                            ans = input()

                            if ans == 'y':
                                os.remove(dst_dir)
                                self.rename_and_move(src, dst)
                                break
                            elif ans == 'n':
                                break
                    else:
                        self.rename_and_move(src, dst)

            elif input_from_user.startswith("mv"):
                if input_from_user == "mv":
                    print("Specify the current name of the file or directory and the new location and/or name")
                    continue
                names = input_from_user.split()
                if len(names) != 3:
                    print("Specify the current name of the file or directory and the new location and/or name")
                    continue
                if not os.path.exists(names[1]):
                    print("No such file or directory")
                if os.path.isdir(names[2]):
                    filename = os.path.basename(names[1])
                    target_path = os.path.join(names[2], filename)
                    if os.path.exists(target_path):
                        print("The file or directory already exists")
                        continue
                elif os.path.exists(names[2]):
                    print("The file or directory already exists")
                    continue

                try:
                    self.rename_and_move(names[1], names[2])
                except FileNotFoundError:
                    print("No such file or directory")

            elif input_from_user.startswith("rm ."):
                input_from_user = input_from_user.split()
                path = self.get_path()
                files = [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))
                         and item.endswith(input_from_user[1])]
                if not files:
                    print(f"File extension {input_from_user[1]} not found in this directory")
                    continue

                self.remove_file_with_extension(input_from_user[1])

            elif input_from_user.startswith("rm"):
                if input_from_user == "rm":
                    print("Specify the file or directory")
                    continue
                input_from_user = input_from_user[3:]

                try:
                    self.remove_file(input_from_user)
                except FileNotFoundError:
                    print("No such file or directory")

            elif input_from_user.startswith("cp ."):
                input_from_user = input_from_user.split()
                if len(input_from_user) != 3:
                    print("Specify the current name of the file or directory and the new location and/or name")
                    continue
                extension = input_from_user[1]
                dst = input_from_user[2]
                path = self.get_path()

                files = [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))
                         and item.endswith(extension)]
                if not files:
                    print(f"File extension {extension} not found in this directory")
                    continue

                for file in files:
                    src = file
                    dst_dir = os.path.join(dst, file)

                    if os.path.exists(dst_dir):
                        while True:
                            print(f"{file} already exists in this directory. Replace? (y/n)")
                            ans = input()

                            if ans == 'y':
                                self.copy_file(src, dst)
                                break
                            elif ans == 'n':
                                break
                    else:
                        self.copy_file(src, dst)

            elif input_from_user.startswith("cp"):
                if input_from_user == "cp":
                    print("Specify the file")
                    continue
                src_and_dst = input_from_user.split()
                if len(src_and_dst) != 3:
                    print("Specify the current name of the file or directory and the new location and/or name")
                    continue
                if not os.path.exists(src_and_dst[1]):
                    print("No such file or directory")
                    continue
                elif os.path.isdir(src_and_dst[2]):
                    filename = os.path.basename(src_and_dst[1])
                    target_path = os.path.join(src_and_dst[2], filename)
                    if os.path.exists(target_path):
                        print(f"{filename} already exists in this directory")
                        continue
                elif os.path.exists(src_and_dst[2]):
                    filename = os.path.basename(src_and_dst[2])
                    print(f"{filename} already exists in this directory")
                    continue

                self.copy_file(src_and_dst[1], src_and_dst[2])

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

    def files_and_subdirectories(self):
        dict_of_directories_and_files = defaultdict(list)
        path = self.get_path()
        list_of_all = os.listdir(path)

        for item in list_of_all:
            if os.path.isdir(item):
                dict_of_directories_and_files['directory'].append(item)
            else:
                dict_of_directories_and_files['file'].append(item)

        return dict_of_directories_and_files

    def files_and_directories_with_size(self):
        dict_of_all = self.files_and_subdirectories()

        for idx, item in enumerate(dict_of_all['file']):
            size = os.stat(item).st_size
            dict_of_all['file'][idx] = (item, size)

        return dict_of_all

    def calculated_size(self):
        dict_of_all = self.files_and_directories_with_size()

        for idx, item in enumerate(dict_of_all['file']):
            size = item[1]
            if size < 1024:
                dict_of_all['file'][idx] = (item[0], f"{round(size)}B")
            elif 1024 <= size < 1024 * 1024:
                size /= 1024
                dict_of_all['file'][idx] = (item[0], f"{round(size)}KB")
            elif 1024 * 1024 <= size < 1024 * 1024 * 1024:
                size /= 1024 * 1024
                dict_of_all['file'][idx] = (item[0], f"{round(size)}MB")
            elif size >= 1024 * 1024 * 1024:
                size /= 1024 * 1024 * 1024
                dict_of_all['file'][idx] = (item[0], f"{round(size)}GB")

        return dict_of_all

    def print_contents(self, type_of_dictionary):

        for item in type_of_dictionary['directory']:
            print(item)

        for item in type_of_dictionary['file']:
            if isinstance(item, tuple):
                print(item[0], item[1])
            else:
                print(item)

    def creating_directory(self, path):
        os.mkdir(path)

    def rename_and_move(self, old_name, new_name):
        shutil.move(old_name, new_name)

    def remove_file(self, path):
        shutil.rmtree(path)

    def remove_file_with_extension(self, extension):
        path = self.get_path()
        for item in os.listdir(path):
            target_path = os.path.join(path, item)
            if os.path.isfile(target_path) and item.endswith(extension):
                os.remove(target_path)

    def copy_file(self, src, dst):
        shutil.copy(src, dst)


