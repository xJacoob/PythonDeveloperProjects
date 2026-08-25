from linguee_page import *
from translator_class import *

def main():
    headers = {'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/93.0.4577.82 Safari/537.36'}
    connection = LingueePage(headers)

    translator = Translator(connection)
    result1, result2 = translator.fetcher()
    print(f"Translations\n{result1}\n{result2}")

if __name__ == "__main__":
    main()