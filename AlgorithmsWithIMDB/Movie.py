class Movie:
    def __init__(self, title, rate):
        self.title = title
        self.rate = rate

    def __str__(self):
        return f"{self.title} - {self.rate}"