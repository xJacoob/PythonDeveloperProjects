import csv
from Movie import Movie

class Reader:
    def __init__(self, path):
        self.path = path
        self.data = []

    def read_csv(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)

            for row in reader:
                movie = Movie(row[0], float(row[1]))
                self.data.append(movie)

        return self.data
