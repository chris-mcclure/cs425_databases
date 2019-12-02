# Generated by Django 2.2.7 on 2019-11-24 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20191123_0015'),
        ('games', '0009_auto_20191123_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='t1Score',
        ),
        migrations.RemoveField(
            model_name='game',
            name='t2Score',
        ),
        migrations.AlterField(
            model_name='game',
            name='teams',
            field=models.ManyToManyField(through='games.GameDetail', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='gamedetail',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
        migrations.AddField(
            model_name='gamedetail',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
    ]
