# Generated by Django 4.2.4 on 2023-09-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinus', '0005_transaction_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('low', 'Низкий'), ('medium', 'Средний'), ('high', 'Высокий')], default='low', max_length=10),
        ),
    ]
