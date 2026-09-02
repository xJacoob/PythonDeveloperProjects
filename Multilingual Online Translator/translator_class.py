from bs4 import BeautifulSoup

class Translator:
    def __init__(self, connection):
        self.connection = connection
        self.languages = {
            1: 'German',
            2: 'English',
            3: 'Spanish',
            4: 'French',
            5: 'Japanese',
            6: 'Dutch',
            7: 'Polish',
            8: 'Portuguese',
            9: 'Romanian',
            10: 'Russian'
        }

    def translate(self):
        target_languages = []
        print("Hello, welcome to the translator. Translator supports:")
        for idx, language in self.languages.items():
            print(f"{idx}. {language}")

        user_number = input("Type the number of your language:\n> ")
        target_number = input("Type the number of language you want to translate to or '0' to translate to all languages:\n> ")
        user_word = input("Type the word you want to translate:\n> ")

        user_language = self.languages[int(user_number)].lower()

        if target_number == '0':
            for key, value in self.languages.items():
                if key == int(user_number):
                    continue
                else:
                    target_languages.append(value.lower())
        else:
            target_languages.append(self.languages[int(target_number)].lower())

        return user_language, target_languages, user_word

    def fetcher(self):
        user_language, target_languages, user_word = self.translate()
        result = []

        for target in target_languages:
            url = f"https://www.linguee.com/{user_language}-{target}/search?source=auto&query={user_word}"
            page = self.connection.fetch(url)

            soup = BeautifulSoup(page.content, 'html.parser')
            valid_class = soup.find('div', class_='exact')

            if valid_class:
                html_words = valid_class.find_all('a', class_='dictLink', href=lambda h: h.startswith(f'/{target}-{user_language}'))
                words = [word.text for word in html_words]
            else:
                words = []

            examples = []
            examples_container = soup.find('div', class_='example_lines inexact')

            if examples_container is not None:
                source_link = examples_container.find_all('a', class_='dictLink', href=lambda h: h.startswith(f'/{user_language}-{target}'))
                target_link = examples_container.find_all('a', class_='dictLink', href=lambda h: h.startswith(f'/{target}-{user_language}'))

                for src, tar in zip(source_link, target_link):
                    examples.append(src.text)
                    examples.append(tar.text)

            result.append((target, words, examples))

        return result, user_word

    def to_file(self):
        result, user_word = self.fetcher()

        with open(f"{user_word}.txt", 'w', encoding='utf-8') as f:
            for lan, words, examples in result:
                print(f"{lan.capitalize()} Translations:", file=f)
                print(f"{lan.capitalize()} Translations:")

                if words:
                    print(words[0], file=f)
                    print(words[0])
                else:
                    print("No translations found.", file=f)
                    print("No translations found.")

                print(f"\n{lan.capitalize()} Examples:", file=f)
                print(f"\n{lan.capitalize()} Examples:")
                if examples:
                    src, trg = examples[0], examples[1]
                    print(src, file=f)
                    print(trg, file=f)
                    print(src)
                    print(trg)
                else:
                    print("No examples found.", file=f)
                    print("No examples found.")

                print(file=f)
                print()
