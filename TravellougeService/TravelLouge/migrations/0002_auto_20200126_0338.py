# Generated by Django 2.2.2 on 2020-01-26 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
        ('Places', '0002_places_leader'),
        ('TravelLouge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travellouge',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user'),
        ),
        migrations.AddField(
            model_name='travellouge',
            name='places',
            field=models.ManyToManyField(to='Places.Places'),
        ),
    ]
