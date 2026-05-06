import os
from ManageCommands import ManageCommands

def main():
    os.chdir('module/root_folder')
    manage_files = ManageCommands()

    manage_files.main_logic()

if __name__ == "__main__":
    main()
