# Generated by Django 2.2.7 on 2019-12-04 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0002_remove_person_ssn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referee', to='persons.Person')),
            ],
        ),
    ]