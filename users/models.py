from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import GeekUserManager
from django.utils import timezone
# Create your models here.

class GeekUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Адрес почты', unique=True)
    is_active = models.BooleanField(verbose_name="Активный", default=True)
    is_staff = models.BooleanField(verbose_name="Модератор", default=False)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="Дата регистрации")
    age = models.SmallIntegerField(verbose_name="Возраст", blank=True),


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []# Можно написать обязательные для заполнения поля

    objects = GeekUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Гик"
        verbose_name_plural = "Гики"