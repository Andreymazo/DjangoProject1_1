from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    phone = models.CharField(max_length=25, verbose_name='телефон')
    country = models.CharField(max_length=30, verbose_name='страна')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватарка')