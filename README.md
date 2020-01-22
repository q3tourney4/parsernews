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
Тело полного запроса:
``` 
{
   "method":"posts",
   "params":{
      "update_news": true, 
      "wizard": "hackernews",
      "order": "title",
      "offset": 10,
      "limit": 10
   },
   "jsonrpc":"2.0",
   "id":"xxx5690xxx"
}

```
Параметр "wizard" и "update_news" являются не обязательными.

Описание параметров:

- "wizard": str - это идентификатор новостного сайта. По умолчанию "hackernews".
- "update_news": bool - это запрос актуальных новостей по требованию. По умолчанию отключен.     
- "order": str - это сортировка по полям БД.
- "offset": int - это смещение в выборке.
- "limit": int - это количество новостей в выборке.

8) Запуск через консоль:
- /parsernews$ export DJANGO_SETTINGS_MODULE=parsernews.settings
- /parsernews$ python app.py

9) Запуск тестов, к примеру, через IDE:
script path: parsernews/parsernews/projectnews/test/test_suite_runner.py

Через консоль:

- /parsernews$ export DJANGO_SETTINGS_MODULE=parsernews.settings
- /parsernews$ coverage run --source=parsernews  parsernews/projectnews/test/test_suite_runner.py && coverage report -m

10) Запуск через Dockerfile:
- docker build -t parsernews-docker .
- docker run -p 8000:8000 --rm -it parsernews-docker
