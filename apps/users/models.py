from django.db import models
from django.contrib.auth.models import AbstractUser
from ..products.models import Product


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='my_profile')
    basket = models.ManyToManyField(Product, blank=True, verbose_name='Корзина', related_name='my_basket')
    bookmarks = models.ManyToManyField(Product, blank=True, verbose_name='Закладки', related_name='my_bookmarks')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


class UserProductRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Очень плохо'),
        (2, 'Пойдет'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Превосходно'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'{self.user.username}: {self.product}, рейтинг: {self.rate}'