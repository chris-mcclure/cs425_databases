# Generated by Django 2.2.7 on 2019-12-02 23:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0012_auto_20191202_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]