# Generated by Django 4.2.7 on 2024-04-07 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название направления')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('experience', models.IntegerField(verbose_name='Стаж')),
                ('add_info', models.CharField(max_length=300, verbose_name='Дополнительная информация')),
                ('directions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagnostics.directions', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
    ]
