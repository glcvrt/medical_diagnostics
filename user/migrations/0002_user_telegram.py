# Generated by Django 5.0.4 on 2024-04-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Telegram'),
        ),
    ]
