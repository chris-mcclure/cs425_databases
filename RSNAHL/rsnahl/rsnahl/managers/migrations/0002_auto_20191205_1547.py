# Generated by Django 2.2.7 on 2019-12-05 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='persons.Person', unique=True),
        ),
    ]