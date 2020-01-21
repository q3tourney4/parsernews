FROM python:3.7-alpine3.7
MAINTAINER Alexander Davydov <avdavydov@reg.ru>
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE parsernews.settings
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/parsernews

WORKDIR /opt/parsernews
COPY requirements.txt /opt/parsernews

# Устанавливаем необходимые зависомости.
RUN pip install --no-cache-dir -r requirements.txt

# Копирование файлов проекта в образ.
COPY . /opt/parsernews/

# Запускаем приложение в контейнере.
CMD python app.py