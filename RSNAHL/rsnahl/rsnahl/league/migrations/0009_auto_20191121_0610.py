# Generated by Django 2.2.7 on 2019-11-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0008_auto_20191121_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='ssn',
            field=models.IntegerField(),
        ),
    ]
