# Generated by Django 2.2.7 on 2019-11-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20191123_0015'),
        ('games', '0006_delete_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='t1',
        ),
        migrations.RemoveField(
            model_name='game',
            name='t2',
        ),
        migrations.AddField(
            model_name='game',
            name='teams',
            field=models.ManyToManyField(to='teams.Team'),
        ),
    ]