from parsernews.projectnews.core.base import Observer, QueryPublisher

# Шаблон для получения новостных данных
class SomeAnotherObserver(Observer):
    def get_news(self, subject: QueryPublisher, order, offset, limit) -> None:
        if subject._service == "www.somesite.com":
            pass
