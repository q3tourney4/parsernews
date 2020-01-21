* Сервис парсинга и получения новостей "parsernews"

Основные инструменты:
- Python 3.8
- Django 3.0.2

Как запустить локально ?

1) Создать виртуальное окружение
python3.8 -m venv parser-news-env
2) Активировать его
. parser-news-env/bin/activate
3) Склонировать проект
4) Поставить зависимости
pip install -r requirements.txt
5) Накатить миграции
6) Запуск приложения, допустим, через IDE: 
script path: /parsernews/projectnews/app.py
environment variables: PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=parsernews.settings
7) Тестирование, к примеру, через Postman. 
Запрос через метод get: http://localhost:8000/
Тело запроса:
``` 
{
   "method":"posts",
   "params":{
      "wizard": "hackernews",
      "order": "title",
      "offset": 10,
      "limit": 10
   },
   "jsonrpc":"2.0",
   "id":"xxx5690xxx"
}
```
Параметр "wizard" является не обязательным.

8) Запуск через консоль:
- /parsernews$ export DJANGO_SETTINGS_MODULE=parsernews.settings
- /parsernews$ python app.py

9) Запуск тестов, к примеру, через IDE:
script path: parsernews/parsernews/projectnews/test/test_suite_runner.py

Через консоль:

- /parsernews$ export DJANGO_SETTINGS_MODULE=parsernews.settings
- /parsernews$ coverage run --source=parsernews  parsernews/projectnews/test/test_suite_runner.py && coverage report -m

Ran 6 tests in 5.040s

OK
Name                                                             Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------------------------
parsernews/__init__.py                                               0      0   100%
parsernews/asgi.py                                                   4      4     0%   10-16
parsernews/projectnews/__init__.py                                   0      0   100%
parsernews/projectnews/admin.py                                      1      0   100%
parsernews/projectnews/api/__init__.py                              12      0   100%
parsernews/projectnews/api/helpers.py                               10      0   100%
parsernews/projectnews/api/resources.py                              7      0   100%
parsernews/projectnews/api/test/__init__.py                          0      0   100%
parsernews/projectnews/api/test/test_helpers.py                     28      1    96%   61
parsernews/projectnews/api/test/test_suites.py                      15      4    73%   27-30
parsernews/projectnews/config.py                                    31      2    94%   29-30
parsernews/projectnews/core/__init__.py                              0      0   100%
parsernews/projectnews/core/base.py                                 31      5    84%   10, 14, 18, 32, 48
parsernews/projectnews/migrations/0001_initial.py                    5      5     0%   3-13
parsernews/projectnews/migrations/__init__.py                        0      0   100%
parsernews/projectnews/models.py                                     5      0   100%
parsernews/projectnews/parcing/__init__.py                           0      0   100%
parsernews/projectnews/parcing/hacker_news_parser.py                29      0   100%
parsernews/projectnews/parcing/test/__init__.py                      0      0   100%
parsernews/projectnews/parcing/test/test_hacker_news_parser.py      19      1    95%   36
parsernews/projectnews/parcing/test/test_suites.py                  15      4    73%   26-29
parsernews/projectnews/sites/__init__.py                             0      0   100%
parsernews/projectnews/sites/hacker_news.py                         15      0   100%
parsernews/projectnews/sites/some_another_site.py                    5      0   100%
parsernews/projectnews/test/__init__.py                              0      0   100%
parsernews/projectnews/test/test_suite_runner.py                    17      1    94%   28
parsernews/settings.py                                              18      0   100%
parsernews/urls.py                                                   3      3     0%   16-19
parsernews/wsgi.py                                                   4      4     0%   10-16
----------------------------------------------------------------------------------------------
TOTAL                                                              274     34    88%

10) Запуск через Dockerfile:
docker build -t parsernews-docker .
docker run -p 8000:8000 --rm -it parsernews-docker
