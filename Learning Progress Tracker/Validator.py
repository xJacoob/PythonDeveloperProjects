import re

class Validator:
    """
    Regex pattern validation
    """

    name_pattern = re.compile(r"^(?!.*['-]{2})[A-Za-z][A-Za-z\-']*[A-Za-z]$")
    last_name_pattern = re.compile(r"^(?!.*['-]{2})[A-Za-z][A-Za-z\-' ]*[A-Za-z]$")
    email_pattern = re.compile(r"^[A-Za-z0-9._\-]+@[A-Za-z0-9]+\.[A-Za-z0-9]+$")
    id_and_points_pattern = re.compile(r"^[A-Za-z0-9]+\s[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+$")

    @classmethod
    def valid_student(cls, student_info: str):
        student_info = student_info.split()

        if len(student_info) < 3:
            return False, "Incorrect credentials."

        name = student_info[0]
        last_name = " ".join(student_info[1:-1])
        email = student_info[-1]

        if not re.fullmatch(cls.name_pattern, name):
            return False, "Incorrect first name."
        elif not re.fullmatch(cls.last_name_pattern, last_name):
            return False, "Incorrect last name."
        elif not re.fullmatch(cls.email_pattern, email):
            return False, "Incorrect email."
        else:
            return True, (name, last_name, email)

    @classmethod
    def valid_id_and_points(cls, id_and_points: str):
        student_id_points = id_and_points.split()

        if not re.fullmatch(cls.id_and_points_pattern, id_and_points):
            return False, "Incorrect points format"

        student_id = student_id_points[0]
        pyt = student_id_points[1]
        dsa = student_id_points[2]
        databases = student_id_points[3]
        flask = student_id_points[4]

        return True, (student_id, pyt, dsa, databases, flask)