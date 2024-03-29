# Generated by Django 2.2.7 on 2019-12-05 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20191205_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='homeTeam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='teams.Team', unique=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='visitingTeam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visiting_team', to='teams.Team', unique=True),
        ),
    ]
