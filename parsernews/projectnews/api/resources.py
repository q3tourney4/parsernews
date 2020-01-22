from typing import Optional, List, Dict

from parsernews.projectnews.api.helpers import validate_paramters
from parsernews.projectnews.api import get_news
from parsernews.projectnews.parcing.hacker_news_parser import parcing_hackernew


def get_posts(
    update_news: bool = False,
    wizard: str = "hackernews",
    order: Optional[str] = "title",
    offset: Optional[int] = 0,
    limit: Optional[int] = 5,
    **kwargs
) -> Optional[List[Dict]]:

    # Создание новостей по требованию
    if update_news:
        parcing_hackernew()

    # Обработка исключительных ситуаций
    if kwargs or not validate_paramters(order, offset, limit):
        return (
            "Некорректные параметры запроса!"
            "Параметры должны быть следующего вида:"
            "limit: 1 до 30."
            "offset: 1 до 10."
            "order: title, url, created."
            "wizard: hackernews. Необязательный параметр."
            "update_news: true/false. Необязательный параметр."
            "Пример запроса: http://0.0.0.0:8000/posts?order=title&offset=10&limit=10"
        )

    return get_news(wizard, order, offset, limit)
