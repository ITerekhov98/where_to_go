from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = HTMLField('Полное описание')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self) -> str:
        return self.title

class Image(models.Model):
    place = models.ForeignKey(
        Place,
        verbose_name='место',
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField('Фото')

    order_number = models.IntegerField(
        'Позиция',
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['order_number']
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'

    def __str__(self) -> str:
        return f'{self.order_number} {self.place}'