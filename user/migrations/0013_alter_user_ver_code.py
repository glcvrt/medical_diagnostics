# Generated by Django 5.0.4 on 2024-04-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='212370406700', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
