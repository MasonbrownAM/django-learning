from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=20, unique=True, verbose_name='شماره تلفن')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی', unique=True)

    class meta:
        verbose_name = 'کاربر'
        verbose_name_plural = verbose_name + 'ان'

    def __str__(self):
        return self.get_full_name()