from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class users(User):
    itinerary=models.CharField(max_length=500)
    is_leader=models.BooleanField(default=False)
    phone_number=models.CharField(max_length=13)
    avatar =models.ImageField(default='/profile/profile.jpg',upload_to='profile')


class Leaders(models.Model):
    userID=models.OneToOneField(users,on_delete=models.CASCADE)
    is_available=models.BooleanField(default=False)
    nationalID=models.CharField(max_length=12)
    has_car=models.BooleanField(default=False)
    car_capacity=models.CharField(max_length=5)
    car_model=models.CharField(max_length=20)
    gender=models.BooleanField(default=False)
    age=models.CharField(max_length=3,default=None)



class Places(models.Model):
    CATEGORY = (
        ("تاریخی", "تاریخی"),
        ("موزه", "موزه"),
        ("جنگل", "جنگل"),
        ("کوه","کوه"),
        ("طبیعت","طبیعت"),
        ("پارک ملی","پارک ملی"),
        ("هنر عمومی","هنر عمومی"),        
        ("مذهبی","مذهبی"),
    )
    leader=models.ManyToManyField(Leaders,related_name='places_leader')
    title = models.CharField(max_length=102, blank=False,default='بدون عنوان')
    Description=models.TextField(default='بدون توضیحات', blank=False)
    Likes = models.CharField(max_length=1, blank=False, null=True,default='0')
    categories=models.CharField(max_length=200,blank=False,null=False,choices=CATEGORY,default=CATEGORY[1][1])
    Hardness=models.CharField(max_length=102, blank=False,default='بدون درجه ی سختی')
    Address=models.CharField(max_length=102, blank=False,default='بدون آدرس ')
    Time=models.CharField(max_length=102, blank=False,default='بدون  تخمین زمان ')
    StartTime=models.CharField(max_length=102, blank=False,default='بدون زمان شروع ')
    EndTime=models.CharField(max_length=102, blank=False,default='بدون زمان پایان ')
    City=models.CharField(max_length=102, blank=False,default='بدون شهر')
    Average=models.CharField(max_length=102, blank=False,default='0')
    image1=models.ImageField(upload_to='image/%Y/%m/%d/',blank=True)
    image2=models.ImageField(upload_to='image/%Y/%m/%d/',blank=True)
    image3=models.ImageField(upload_to='image/%Y/%m/%d/',blank=True)
    
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title



class TravelLouges(models.Model):
    auther=models.ForeignKey(users,on_delete=models.CASCADE,related_name='travellouge_author')
    title = models.CharField(max_length=102)
    description=models.CharField(max_length=1000)
    image1=models.ImageField(upload_to='image/%Y/%m/%d/',default='travellouge/defualt.jpg')
    image2=models.ImageField(upload_to='image/%Y/%m/%d/',default='travellouge/defualt.jpg')
    image3=models.ImageField(upload_to='image/%Y/%m/%d/',default='travellouge/defualt.jpg')
    place=models.ManyToManyField(Places,related_name='visitedplaces_travellogue')  

