from Validator import Validator
from Students import Students
from Statistic import Statistic

class UserInterface:
    """
    User interface class
    """

    def main_logic(self):
        print("Learning Progress Tracker")

        while True:
            user_command = input("")
            if user_command == "exit":
                self.exit_command()
            elif not user_command.strip():
                print("No input")
            elif user_command == "add students":
                self.add_student()
            elif user_command == "back":
                print("Enter 'exit' to exit the program.")
            elif user_command == "list":
                self.list_students()
            elif user_command == "add points":
                self.add_points()
            elif user_command == "find":
                self.list_points()
            elif user_command == "statistics":
                self.list_statistics()
            elif user_command == "notify":
                self.notify_student()
            else:
                print("Unknown command!")

    @staticmethod
    def exit_command():
        print("Bye!")
        exit()

    @staticmethod
    def add_student():
        print("Enter student credentials or 'back' to return:")
        while True:
            user_input = input("")

            if user_input == "back":
                print(f"Total {Students.number_of_students} students have been added.")
                break

            is_valid, information = Validator.valid_student(user_input)

            if is_valid:
                name, last_name, email = information

                if not Students.is_email_available(email):
                    print("This email is already taken.")

                else:
                    new_student = Students(name, last_name, email)
                    Students.add_student(new_student)
                    print("The student has been added.")

            else:
                print(information)

    @staticmethod
    def list_students():
        if not Students.student_information:
            print("No students found")

        print("Students: ")
        for key in Students.student_information:
            print(key)

    @staticmethod
    def add_points():
        print("Enter an id and points or 'back' to return:")
        while True:
            user_input = input("")

            if user_input == "back":
                break

            is_valid, id_points = Validator.valid_id_and_points(user_input)

            if is_valid:
                student_id = id_points[0]
                points = id_points[1:]

                if student_id not in Students.student_information:
                    print(f"No student is found for id={student_id}")
                    continue

                Students.update_points(student_id, points)
                print("Points updated")

            else:
                print(id_points)

    @staticmethod
    def list_points():
        print("Enter an id or 'back' to return")

        while True:
            user_input = input("")

            if user_input == "back":
                break

            is_exist, points = Students.check_student_points(user_input)

            if is_exist:
                print(points)
            else:
                print(points)

    @staticmethod
    def list_statistics():
        print("Type the name of a course to see details or 'back' to quit:")

        courses = {
            "python": "Python",
            "dsa": "DSA",
            "databases": "Databases",
            "flask": "Flask"
        }

        Statistic.most_and_least_popular(Students.student_information)
        Statistic.highest_and_lowest_activity()
        Statistic.hardest_and_easiest_courses(Students.student_information)

        for rank, course in Statistic.statistics.items():
            print(f"{rank}: {course}")

        while True:
            user_input = input("").lower()

            if user_input == "back":
                break

            elif user_input in courses:
                correct_course_name = courses[user_input]
                UserInterface.list_details(correct_course_name)

            else:
                print("Unknown course!")

    @staticmethod
    def list_details(which_course: str):
        details = Statistic.details(Students.student_information, which_course)

        print(which_course)
        print("id     points    completed")

        for value in details:
            print(f"{value[0]}     {value[1]}     {value[2]}%")

    @staticmethod
    def notify_student():
        notified_students = 0
        thresholds = Statistic.points_to_complete
        for key, student in Students.student_information.items():
            is_completed = student.who_complete_course(thresholds)

            if is_completed:
                for course in is_completed:
                    print(f"To: {student.email}")
                    print(f"Re: Your Learning Progress\nHello, {student.name} {student.last_name}! You have accomplished our {course} course!")

                notified_students += 1

        print(f"Total {notified_students} students have been notified.")