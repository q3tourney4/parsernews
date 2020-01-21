from django.db import models


class NewsAggregator(models.Model):
    """
    Сборник новостей
    """

    title = models.CharField("Заголовок новости", max_length=1024, default="")
    url = models.CharField("url новости", max_length=2048, default="")
    created = models.DateTimeField("Дата новости", null=True)
