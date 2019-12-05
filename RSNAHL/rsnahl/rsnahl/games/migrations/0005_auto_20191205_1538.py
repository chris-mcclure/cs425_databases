# Generated by Django 2.2.7 on 2019-12-05 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20191205_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='homeTeam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='teams.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='visitingTeam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visiting_team', to='teams.Team'),
        ),
    ]