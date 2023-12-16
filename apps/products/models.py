from django.contrib.auth import get_user_model
from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=18, verbose_name='Название атрибута')
    value = models.CharField(max_length=24, verbose_name='Значение атрибута')

    def __str__(self):
        return f'{self.name}: {self.value}'

    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'


class Image(models.Model):
    image = models.ImageField(upload_to='media/images/products/')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return 'Изображение'

class Product(models.Model):
    name = models.CharField(max_length=48, verbose_name='Название')
    description = models.TextField(max_length=1500, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    images = models.ManyToManyField(Image, related_name='product_images', verbose_name='Изображения')
    attributes = models.ManyToManyField(Attribute, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


