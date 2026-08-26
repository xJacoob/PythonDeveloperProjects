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

        examples = []

        context_line = valid_class.find_all('span', class_='tag_e')

        for line in context_line:
            source_span = line.find('span', class_='tag_s')
            target_span = line.find('span', class_='tag_t')
            if source_span and target_span:
                examples.append(source_span.text)
                examples.append(target_span.text)

        examples_container = soup.find('div', class_='example_lines inexact')

        if examples_container is not None:
            if lan == "fr":
                source_link = examples_container.find_all('a', class_='dictLink', href=lambda h: h.startswith('/english-french'))
                target_link = examples_container.find_all('a', class_='dictLink', href=lambda h: h.startswith('/french-english'))
            else:
                source_link = examples_container.find_all('a', class_='dictLink', href=lambda h: h.startswith('/french-english'))
                target_link = examples_container.find_all('a', class_='dictLink', href=lambda h: h.startswith('/english-french'))


            for source, target in zip(source_link, target_link):
                examples.append(source.text)
                examples.append(target.text)

        return words, examples, lan

    def output(self):
        words, examples, lan = self.fetcher()

        if lan == "fr":
            print("\nFrench Translations:")
        else:
            print("\nEnglish Translations:")

        for word in words:
            print(word)

        if lan == "fr":
            print("\nFrench Examples:")
        else:
            print("\nEnglish Examples:")

        for i in range(0, len(examples), 2):
            pair = examples[i:i + 2]
            print(*pair, sep='\n')
            if i + 2 < len(examples):
                print()
