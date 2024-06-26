# Generated by Django 5.0.4 on 2024-04-12 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostics', '0003_alter_directions_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Стоимость')),
                ('directions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='услуги', to='diagnostics.directions', verbose_name='Направление')),
                ('doctor', models.ManyToManyField(related_name='Врач', to='diagnostics.doctor')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
