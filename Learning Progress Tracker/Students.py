class Students:

    student_id = 10000
    student_information = {}
    number_of_students = 0
    students_emails = set()
    course_activity = {
        "Python": 0,
        "DSA": 0,
        "Databases": 0,
        "Flask": 0
    }
    """
    Students credentials
    """
    def __init__(self, name: str, last_name: str, email: str):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.points = {
            "Python": 0,
            "DSA": 0,
            "Databases": 0,
            "Flask": 0
        }
        self.completed_courses = set()

    @classmethod
    def add_student(cls, student: Students):
        cls.student_information[str(cls.student_id)] = student
        cls.student_id += 1
        cls.number_of_students += 1

    @classmethod
    def is_email_available(cls, email: str) -> bool:
        if email in cls.students_emails:
            return False

        Students.students_emails.add(email)
        return True

    @classmethod
    def update_points(cls, student_id: str, points: list):
        for key, value in zip(cls.student_information[student_id].points, points):
            cls.student_information[student_id].points[key] += int(value)

            if int(value) > 0:
                cls.course_activity[key] += 1

    @classmethod
    def check_student_points(cls, identifier: str):
        if identifier not in cls.student_information:
            return False, f"No student is found for id={identifier}"

        student = cls.student_information[identifier]

        python = student.points["Python"]
        dsa = student.points["DSA"]
        databases = student.points["Databases"]
        flask = student.points["Flask"]

        return True, f"{identifier} points: Python={python}; DSA={dsa}; Databases={databases}; Flask={flask}"

    def who_complete_course(self, thresholds: dict) -> list:
        just_completed = []
        for course, points in self.points.items():
            if points >= thresholds[course] and course not in self.completed_courses:
                self.completed_courses.add(course)
                just_completed.append(course)

        return just_completed



