import datetime
import json

import django

django.setup()

from parsernews.projectnews.core.base import Observer, QueryPublisher
from parsernews.projectnews.models import NewsAggregator


def date_converter(value):
    if isinstance(value, datetime.datetime):
        return value.__str__()


class HackerNewsObserver(Observer):
    def get_news(self, subject: QueryPublisher, order, offset, limit) -> None:
        if subject._service == "hackernews":
            elements = (
                NewsAggregator.objects.all()
                .values("title", "url", "created")
                .order_by(order)[offset : offset + limit]
            )

            result = [
                {
                    "title": x["title"],
                    "url": x["url"],
                    "created": json.dumps(x["created"], default=date_converter),
                }
                for x in elements
            ]

            subject.answer = result
