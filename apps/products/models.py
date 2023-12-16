from django.db import models
from api import validate_image_count


class Attribute(models.Model):
    name = models.CharField(max_length=16, verbose_name='Название атрибута')
    value = models.CharField(max_length=24, verbose_name='Значение атрибута')

    def __str__(self):
        return f'{self.name}: {self.value}'

    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'


class Image(models.Model):
    image = models.ImageField(upload_to='images/products/')


class Product(models.Model):
    name = models.CharField(max_length=48, verbose_name='Название')
    description = models.TextField(max_length=1500, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    images = models.ManyToManyField(Image, validators=[validate_image_count], related_name='product-images', verbose_name='Изображения')
    attributes = models.ManyToManyField(Attribute, blank=True)
