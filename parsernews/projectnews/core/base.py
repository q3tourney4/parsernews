from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class Publisher(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, order, offset, limit) -> None:
        pass


class QueryPublisher(Publisher):
    _service: str = None

    _observers: List[Observer] = []

    answer: List[Dict] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, order, offset, limit) -> None:

        for observer in self._observers:
            observer.get_news(self, order, offset, limit)

    def notify_subscribers(self, wizard, order, offset, limit) -> None:
        self._service = wizard
        self.notify(order, offset, limit)


class Observer(ABC):
    @abstractmethod
    def get_news(self, subject: QueryPublisher, order, offset, limit) -> None:
        pass
