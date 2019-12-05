# Generated by Django 2.2.7 on 2019-12-05 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0004_auto_20191205_1610'),
        ('coaches', '0001_initial'),
        ('teams', '0007_delete_teamscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='coach',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_coach', to='coaches.Coach'),
        ),
        migrations.AddField(
            model_name='team',
            name='manager',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_manager', to='managers.Manager'),
        ),
    ]
