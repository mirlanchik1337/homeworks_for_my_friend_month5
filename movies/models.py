from django.db.models import *


class Director(Model):
    name = CharField(max_length=50, default='None', verbose_name='Имя Директора')

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=100, unique=True, blank=True, verbose_name='Название Фильма')
    description = TextField(max_length=255, default='', blank=True, null=True, verbose_name='описание')
    duration = FloatField(default=0, verbose_name='Продолжительность')
    director = ForeignKey(Director, on_delete=CASCADE)

    def __str__(self):
        return self.title


class Review(Model):
    text = TextField(max_length=1000, default=0, verbose_name='Отзыв')
    movie = ForeignKey(Movie, on_delete=CASCADE)

    def __str__(self):
        return self.text

