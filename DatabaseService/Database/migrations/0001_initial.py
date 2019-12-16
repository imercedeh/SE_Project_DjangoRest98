# Generated by Django 2.1.2 on 2019-12-16 13:44

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=False)),
                ('nationalID', models.CharField(max_length=12)),
                ('has_car', models.BooleanField(default=False)),
                ('car_capacity', models.CharField(max_length=5)),
                ('car_model', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=False)),
                ('age', models.CharField(default=None, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='بدون عنوان', max_length=102)),
                ('Description', models.TextField(default='بدون توضیحات')),
                ('Likes', models.CharField(default='0', max_length=1, null=True)),
                ('categories', models.CharField(choices=[('تاریخی', 'تاریخی'), ('موزه', 'موزه'), ('جنگل', 'جنگل'), ('کوه', 'کوه'), ('طبیعت', 'طبیعت'), ('پارک ملی', 'پارک ملی'), ('هنر عمومی', 'هنر عمومی'), ('مذهبی', 'مذهبی')], default='موزه', max_length=200)),
                ('Hardness', models.CharField(default='بدون درجه ی سختی', max_length=102)),
                ('Address', models.CharField(default='بدون آدرس ', max_length=102)),
                ('Time', models.CharField(default='بدون  تخمین زمان ', max_length=102)),
                ('StartTime', models.CharField(default='بدون زمان شروع ', max_length=102)),
                ('EndTime', models.CharField(default='بدون زمان پایان ', max_length=102)),
                ('City', models.CharField(default='بدون شهر', max_length=102)),
                ('Average', models.CharField(default='0', max_length=102)),
                ('image1', models.ImageField(blank=True, upload_to='image/%Y/%m/%d/')),
                ('image2', models.ImageField(blank=True, upload_to='image/%Y/%m/%d/')),
                ('image3', models.ImageField(blank=True, upload_to='image/%Y/%m/%d/')),
                ('leader', models.ManyToManyField(related_name='places_leader', to='Database.Leader')),
            ],
        ),
        migrations.CreateModel(
            name='TravelLouges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=102)),
                ('description', models.CharField(max_length=1000)),
                ('image1', models.ImageField(default='travellouge/defualt.jpg', upload_to='image/%Y/%m/%d/')),
                ('image2', models.ImageField(default='travellouge/defualt.jpg', upload_to='image/%Y/%m/%d/')),
                ('image3', models.ImageField(default='travellouge/defualt.jpg', upload_to='image/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('itinerary', models.CharField(max_length=500)),
                ('is_leader', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=13)),
                ('avatar', models.ImageField(default='/profile/profile.jpg', upload_to='profile')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='travellouges',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.user'),
        ),
        migrations.AddField(
            model_name='travellouges',
            name='places',
            field=models.ManyToManyField(to='Database.Places'),
        ),
        migrations.AddField(
            model_name='leader',
            name='userID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Database.user'),
        ),
    ]
