# Generated by Django 2.2.7 on 2019-11-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_auto_20191124_0717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='date',
        ),
        migrations.AddField(
            model_name='gamedetail',
            name='date',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
    ]