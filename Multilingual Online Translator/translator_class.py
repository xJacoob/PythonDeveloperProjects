from bs4 import BeautifulSoup

class Translator:
    def __init__(self, connection):
        self.connection = connection

    @staticmethod
    def translate():
        user_lan = input('Type "en" if you want to translate from French into English,'
                            'or "fr" if you want to translate from English into French:\n> ')

        print("Type the word you want to translate:")
        user_word = input("> ")
        print(f'You chose "{user_lan}" as a language to translate "{user_word}".')

        if user_lan == 'fr':
            return f"https://www.linguee.com/english-french/search?source=auto&query={user_word}", user_lan
        else:
            return f"https://www.linguee.com/french-english/search?source=auto&query={user_word}", user_lan

    def fetcher(self):
        url, lan = self.translate()
        page = self.connection.fetch(url)

        if page.status_code == 200:
            print("200 OK")

        soup = BeautifulSoup(page.content, 'html.parser')
        valid_class = soup.find('div', class_='exact')

        if lan == "fr":
            html_words = valid_class.find_all('a', class_='dictLink', href=lambda h: h.startswith('/french-english'))
        else:
            html_words = valid_class.find_all('a', class_='dictLink', href=lambda h: h.startswith('/english-french'))

        words = [word.text for word in html_words]

        examples_container = soup.find('div', class_='example_lines inexact')
        examples = []

        if lan == "fr":
            source_link = examples_container.find_all('a', class_='dictLink', href=lambda h: h.startswith('/english-french'))
            target_link = examples_container.find_all('a', class_='dictLink', href=lambda h: h.startswith('/french-english'))
        else:
            source_link = examples_container.find_all('a', class_='dictLink', href=lambda h: h.startswith('/french-english'))
            target_link = examples_container.find_all('a', class_='dictLink', href=lambda h: h.startswith('/english-french'))


        for source, target in zip(source_link, target_link):
            examples.append(source.text)
            examples.append(target.text)

        return words, examples




