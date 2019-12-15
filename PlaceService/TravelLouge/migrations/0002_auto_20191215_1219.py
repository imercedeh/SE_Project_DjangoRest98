# Generated by Django 2.2.2 on 2019-12-15 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TravelLouge', '0001_initial'),
        ('Users', '0001_initial'),
        ('Places', '0002_places_leader'),
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
