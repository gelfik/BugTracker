import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.contrib.auth.models import Group


class UserManager(BaseUserManager):
    def create_user(self, username, email, last_name, first_name, password=None):
        if username is None:
            raise TypeError('Username обязательное поле.')
        if email is None:
            raise TypeError('Email обязательное поле.')
        if last_name is None:
            raise TypeError('Фамилия обязательное поле.')
        if last_name is None:
            raise TypeError('Имя обязательное поле.')

        user = self.model(username=username, email=self.normalize_email(email), first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, last_name, first_name, password):
        if username is None:
            raise TypeError('Username обязательное поле.')
        if email is None:
            raise TypeError('Email обязательное поле.')
        if last_name is None:
            raise TypeError('Фамилия обязательное поле.')
        if first_name is None:
            raise TypeError('Имя обязательное поле.')
        if password is None:
            raise TypeError('Пароль обязательное поле.')

        user = self.create_user(username, email, last_name, first_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField('Дата регистрации', auto_now_add=True)
    updated_at = models.DateTimeField('Дата последнего изменения', auto_now=True)
    last_name = models.CharField('Фамилия', max_length=255, default=None)
    first_name = models.CharField('Имя', max_length=255, default=None)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'email', ]

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'Users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        return jwt.encode({'user_data': {'id': self.pk, 'username': self.username,
                                         'created_date': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))},
                           'exp': datetime.now() + timedelta(days=60),
                           'iat': datetime.now(),
                           }, settings.SECRET_KEY, algorithm='HS256')
