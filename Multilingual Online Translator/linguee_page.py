import requests

class LingueePage:
    def __init__(self, headers):
        self.headers = headers

    def fetch(self, url):
        page = requests.get(url, headers=self.headers)
        return page