from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from users.models import CustomUser


class Todo(models.Model):
    DONE = 'done'
    NOT_PERFORMED = 'not performed'
    STATUS = (
        (DONE, 'done'),
        (NOT_PERFORMED, 'not performed')
    )
    MANAGER = 'manager'
    DEVELOPER = 'developer'
    TYPE_USER = (
        (MANAGER, 'manager'),
        (DEVELOPER, 'developer')
    )
    title = models.CharField(verbose_name='заголовок', max_length=128, blank=False)
    description = models.TextField(verbose_name='описание', blank=False)
    created_at = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    deadline = models.DateTimeField(verbose_name='дедлайн', default=(now() + timedelta(hours=48)))
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=CustomUser)
    status = models.CharField(
        verbose_name='Статус', 
        max_length=15, 
        choices=STATUS,
        default=NOT_PERFORMED
    )

    def __str__(self):
        return self.title