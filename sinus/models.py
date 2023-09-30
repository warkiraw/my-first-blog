
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import Group


class Transaction(models.Model):
    TYPE_CHOICES = (
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    )
    STATUS_CHOICES = (
        ('new', 'NEW'),
        ('resolved', 'Решена'),
        ('in_progress', 'В процессе')
    )
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=10_000, blank=True, null=True)
    description = models.CharField(max_length=10_000, blank=True, null=True)
    amount = models.CharField(max_length=10_000, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='low')
    status = models.CharField(max_length=11, choices=STATUS_CHOICES,default='NEW')
    def __str__(self):
        return f"{self.description}: {self.amount} {self.created_date} {self.type} {self.status} {self.name} {self.email}"
    def amount_abs(self) -> int:
        return int(self.amount)

