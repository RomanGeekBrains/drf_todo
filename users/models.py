from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER = (
        ('m', 'мужчина'),
        ('f', 'женщина'),
    )
    gender = models.CharField(max_length=1, verbose_name='пол', choices=GENDER, default='')
    email = models.EmailField(max_length=254, unique=True, verbose_name="электронная почта", blank=False)
    