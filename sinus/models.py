from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    PRIORITY_CHOICES = (
        ('high', 'Высокий'),
        ('medium', 'Средний'),
        ('low', 'Низкий'),
    )
    tema = models.CharField(max_length=40)
    text = models.TextField()
    priority = models.CharField(max_length=10,choices= PRIORITY_CHOICES,default='medium')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.tema