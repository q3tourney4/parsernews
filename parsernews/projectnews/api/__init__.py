from typing import Optional

from parsernews.projectnews.core.base import QueryPublisher
from parsernews.projectnews.sites.hacker_news import HackerNewsObserver
from parsernews.projectnews.sites.some_another_site import SomeAnotherObserver

# Издатель
publisher = QueryPublisher()

# Подписчики
hackernews = HackerNewsObserver()
some_another_news = SomeAnotherObserver()

# Назначим подписку
publisher.attach(hackernews)
publisher.attach(some_another_news)


def get_news(
    wizard: str,
    order: Optional[str] = None,
    offset: Optional[int] = None,
    limit: Optional[int] = None,
):
    publisher.notify_subscribers(wizard, order, offset, limit)

    return publisher.answer
