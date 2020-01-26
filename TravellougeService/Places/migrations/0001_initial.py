# Generated by Django 2.2.2 on 2020-01-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            ],
        ),
    ]
