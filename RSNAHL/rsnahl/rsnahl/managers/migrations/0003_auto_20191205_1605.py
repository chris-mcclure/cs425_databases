# Generated by Django 2.2.7 on 2019-12-05 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0002_auto_20191205_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='manager',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='persons.Person'),
        ),
    ]
