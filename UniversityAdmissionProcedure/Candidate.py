class Candidate:
    def __init__(self, name: str, surname: str, priorities: list, physics: float, chemistry: float, math: float, computer_science: float):
        self.name = name
        self.surname = surname
        self.priorities = priorities
        self.is_accepted = False
        self.student_department = None
        self.exams = {
            'Physics': (physics + math) / 2,
            'Chemistry': chemistry,
            'Mathematics': math,
            'Engineering': (computer_science + math) / 2,
            'Biotech': (chemistry + physics) / 2
        }

    def __str__(self):
        return f"{self.name} {self.surname} {self.exams[self.student_department]}"