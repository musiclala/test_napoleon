from datetime import datetime, timedelta

import PIL.Image
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import jwt

from test_napoleon import settings


class User(AbstractBaseUser):
    """Модель пользователя"""
    email = models.EmailField(verbose_name='Email', unique=True)
    password = models.CharField(verbose_name='Password', max_length=30)
    surname = models.CharField(verbose_name='Surname', max_length=30)
    name = models.CharField(verbose_name='Name', max_length=30)
    number_phone = models.CharField(verbose_name='Number Phone', max_length=11)
    avatar = models.ImageField(verbose_name='Avatar', upload_to='photos/%Y/%m/%d/', blank=True)
    companies = models.ManyToManyField("Company", related_name='users')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def _generate_jwt_token(self):
        """Получаем токен"""
        dt = (datetime.now() + timedelta(days=1)).day

        token = jwt.encode({
            'id': self.pk,
            'exp': str(dt).strftime('%s')
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    @property
    def token(self):
        return self._generate_jwt_token()

    def save(self, *args, **kwargs):
        """Меняем картинку"""
        super(User, self).save(*args, **kwargs)
        if self.avatar:
            filepath = self.avatar.path
            width = self.avatar.width
            height = self.avatar.height

            if height > 300 or width > 300:
                image = PIL.Image.open(filepath)
                image = image.resize((200, 200))
                image.save(filepath)


class Company(models.Model):
    """ Модель организации"""
    name = models.CharField(verbose_name='Name', max_length=50)
    description = models.CharField(verbose_name='Description', max_length=100)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
