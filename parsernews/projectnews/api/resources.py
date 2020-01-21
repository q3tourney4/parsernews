from typing import Optional, List, Dict

from parsernews.projectnews.api.helpers import validate_paramters
from parsernews.projectnews.api import get_news
from parsernews.projectnews.parcing.hacker_news_parser import parcing_hackernew


def get_posts(
    wizard: str = "hackernews",
    order: Optional[str] = "title",
    offset: Optional[int] = 0,
    limit: Optional[int] = 5,
    **kwargs
) -> Optional[List[Dict]]:

    # Создание новостей по требованию
    parcing_hackernew()

    # Обработка исключительных ситуаций
    if kwargs or not validate_paramters(order, offset, limit):
        return (
            "Некорректные параметры запроса!"
            "Параметры должны быть следующего вида:"
            "limit: 1 до 30."
            "offset: 1 до 10."
            "order: title, url, created."
            "Пример запроса: http://localhost:8000/posts?order=title&offset=10&limit=10"
        )

    return get_news(wizard, order, offset, limit)
