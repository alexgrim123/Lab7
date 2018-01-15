from django.db import models


class Book(models.Model):
        name_book = models.CharField(max_length=100)
        price_book = models.IntegerField(default=36)


class Writer (models.Model):
        writer_fio = models.CharField(max_length=100)
        writer_book = models.CharField(max_length=100)
