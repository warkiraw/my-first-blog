# Generated by Django 4.2.4 on 2023-09-16 09:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sinus', '0004_transaction_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
