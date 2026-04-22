class Department:
    def __init__(self, department_name: str, capacity: int):
        self.department_name = department_name
        self.capacity = capacity
        self.accepted_students = []

    def print_department(self):
        print(self.department_name)
        sorted_list = sorted(self.accepted_students, key=lambda x: (-x.exams[self.department_name], x.name, x.surname))
        for student in sorted_list:
            print(student)