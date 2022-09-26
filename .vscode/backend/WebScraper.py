import requests
from bs4 import BeautifulSoup

class WebScraper:

    def youaregay():
        URL = "https://realpython.github.io/fake-jobs/"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="ResultsContainer")
        return page.text

