# Generated by Django 2.2.7 on 2019-11-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0009_auto_20191121_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_initial',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='pob',
            field=models.CharField(max_length=200),
        ),
    ]
