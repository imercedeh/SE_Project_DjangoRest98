# Generated by Django 2.2.2 on 2019-12-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Places', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='leader',
            field=models.ManyToManyField(to='Users.Leader'),
        ),
    ]
