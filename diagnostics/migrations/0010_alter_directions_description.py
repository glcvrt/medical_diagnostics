# Generated by Django 5.0.4 on 2024-04-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostics', '0009_delete_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directions',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
    ]
