import sqlite3

class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('card.s3db')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS card (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0)
        ''')
        self.connection.commit()

    def add_card(self, number, pin):
        self.cursor.execute(
            'INSERT INTO card (number, pin) VALUES (?, ?)',
            (number, pin)
        )
        self.connection.commit()

    def find_by_partial_number(self, pattern):
        self.cursor.execute('SELECT * FROM card WHERE number = (?)', (pattern,))
        return self.cursor.fetchone()

    def find_by_number_and_pin(self, number, pin) -> tuple:
        self.cursor.execute('SELECT * FROM card WHERE number = (?) AND pin = (?)', (number, pin))
        return self.cursor.fetchone()

