import os

import yaml
from django.conf import settings


__all__ = ["config"]


class ConfigDir:
    def __init__(self, name):
        self.__name = name
        self.__config = None

    def __load(self):
        if self.__config is not None:
            return

        path = os.path.join(
            settings.BASE_DIR, "parsernews/projectnews/cfg", f"{self.__name}.yaml"
        )

        with open(path) as f:
            self.__config = yaml.load(f, Loader=yaml.SafeLoader)

    def __getitem__(self, item):
        self.__load()
        return self.__config[item]

    def __getattr__(self, item):
        self.__load()
        return getattr(self.__config, item)


class Config:
    def __init__(self):
        self.__cache = {}

    def __load(self, name):
        if name in self.__cache:
            return
        self.__cache[name] = ConfigDir(name)

    def __getitem__(self, item):
        self.__load(item)
        return self.__cache[item]


config = Config()
