# Generated by Django 2.2.7 on 2019-12-02 23:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_referee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
    ]
