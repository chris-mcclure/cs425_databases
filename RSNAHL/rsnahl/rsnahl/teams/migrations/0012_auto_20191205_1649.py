# Generated by Django 2.2.7 on 2019-12-05 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0011_auto_20191205_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_coach', to='coaches.Coach'),
        ),
    ]
