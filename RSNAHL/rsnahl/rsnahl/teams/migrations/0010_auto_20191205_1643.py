# Generated by Django 2.2.7 on 2019-12-05 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('teams', '0009_auto_20191205_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='coach',
        ),
        migrations.AddField(
            model_name='team',
            name='coach',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_coach', to='coaches.Coach'),
        ),
    ]
