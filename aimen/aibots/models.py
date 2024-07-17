from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Aibot(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField('Создание', auto_now_add=True)
    updated_at = models.DateTimeField('Изменение', auto_now=True)

    def __str__(self):
        return f'Bot id: {self.pk}, bot name: {self.name}'
    

class AibotOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=255)
    requirements = models.TextField('Требования', max_length=2000)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField('Создание', auto_now_add=True)
    updated_at = models.DateTimeField('Изменение', auto_now=True)

    def __str__(self):
        return f'Order id: {self.pk}, user id: {self.user_id}'