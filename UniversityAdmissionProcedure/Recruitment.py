from typing import List
from Candidate import Candidate
from Department import Department

class Recruitment:
    def __init__(self, capacity: int, all_applicants: List[Candidate]):
        self.capacity = capacity
        self.all_applicants = all_applicants
        self.departments = {
            'Engineering': Department('Engineering', capacity),
            'Biotech': Department('Biotech', capacity),
            'Chemistry': Department('Chemistry', capacity),
            'Physics': Department('Physics', capacity),
            'Mathematics': Department('Mathematics', capacity)
        }

    def allocation(self):
        for tour in range(3):
            for key, value in self.departments.items():
                temp_list = []
                for student in self.all_applicants:
                    if student.priorities[tour] == key and not student.is_accepted:
                        temp_list.append(student)
                sorted_list = sorted(temp_list, key=lambda x: (-x.exams[key], x.name, x.surname))
                for winner_student in sorted_list:
                    if len(self.departments[key].accepted_students) < self.capacity:
                        self.departments[key].accepted_students.append(winner_student)
                        winner_student.is_accepted = True
                        winner_student.student_department = key
                else:
                    continue

    def print_result(self):
        departments = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
        for department in departments:
            self.departments[department].print_department()
            print()

    def write_to_file(self):
        for key, value in self.departments.items():
            department_name = key.lower()
            with open(department_name + '.txt', 'w') as file:
                department_name = key.capitalize()
                sorted_list = sorted(value.accepted_students,
                                     key=lambda x: (-x.exams[department_name], x.name, x.surname))
                for student in sorted_list:
                    file.write(f'{student.name} {student.surname} {student.exams[key]}\n')