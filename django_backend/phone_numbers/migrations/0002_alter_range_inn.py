# Generated by Django 5.0.6 on 2024-05-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_numbers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='range',
            name='inn',
            field=models.BigIntegerField(),
        ),
    ]
