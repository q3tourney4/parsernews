import unittest
import urllib.request
from bs4 import BeautifulSoup

from parsernews.projectnews.parcing.hacker_news_parser import (
    get_elements_news,
    parcing_hackernew,
)


class HackerNewsParserTest(unittest.TestCase):

    # Тестирование функции get_elements_news

    # Позитивные тесты
    def test_get_elements_news_positive(self):
        url = "https://news.ycombinator.com/"
        web_url_data = urllib.request.urlopen(url)
        html_data = web_url_data.read()
        page = BeautifulSoup(html_data, "html.parser")
        specific_data = page.findAll("tr")[3].findAll(
            "td", {"class": "title", "align": ""}
        )

        result = get_elements_news(specific_data=specific_data, from_news=0, to_news=30)
        self.assertTrue(list, result)

    # Негативные тесты
    def test_get_elements_news_negative(self):
        self.assertRaises(
            TypeError, get_elements_news, specific_data=True, from_news=-1, to_news=150
        )

    # Тестирование функции parcing_hackernew
    # Позитивные тесты
    def test_parcing_hackernew(self):
        self.assertIsNone(parcing_hackernew())


if __name__ == "__main__":
    unittest.main()
