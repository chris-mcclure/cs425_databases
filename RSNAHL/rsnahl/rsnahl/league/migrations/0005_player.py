# Generated by Django 2.2.7 on 2019-11-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_auto_20191120_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('height', models.CharField(default='', max_length=10)),
                ('position', models.CharField(default='', max_length=20)),
                ('stick_orientation', models.CharField(default='', max_length=5)),
            ],
        ),
    ]
