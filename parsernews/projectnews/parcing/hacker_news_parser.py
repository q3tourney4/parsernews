import datetime
import django
import urllib.request

from bs4 import BeautifulSoup
from django.utils.timezone import make_aware
from typing import List

from parsernews.projectnews.models import NewsAggregator
from parsernews.projectnews.config import config

django.setup()


def get_elements_news(specific_data, from_news, to_news) -> List:
    elements_news = []
    for data in specific_data[from_news:to_news]:
        header = data.text
        url = None
        for link in data.find_all("a", href=True):
            url = link["href"]
        elements_news.append({"title": header, "url": url.replace("from?site=", "")})
    return elements_news


def parcing_hackernew() -> None:
    # Данные из конфигурационного файла
    url = config["news"]["sites"]["hackernews_url"]
    limit_news = config["news"]["sites"]["hackernews_count"]
    hackernews_start_tracker = config["news"]["sites"]["hackernews_start_tracker"]

    web_url_data = urllib.request.urlopen(url)

    html_data = web_url_data.read()

    page = BeautifulSoup(html_data, "html.parser")

    specific_data = page.findAll("tr")[hackernews_start_tracker].findAll(
        "td", {"class": "title", "align": ""}
    )

    elements_news = get_elements_news(specific_data, 0, limit_news)

    # TODO Только топ новостей. Убрать если нужны все новости.
    NewsAggregator.objects.all().delete()

    NewsAggregator.objects.bulk_create(
        NewsAggregator(
            title=row["title"],
            url=row["url"],
            created=make_aware(datetime.datetime.now()).isoformat(),
        )
        for row in elements_news
    )
