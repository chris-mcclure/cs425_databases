# Generated by Django 2.2.7 on 2019-11-22 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='ssn',
        ),
    ]