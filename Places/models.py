from django.db import models

# Create your models here.

class Places(models.Model):
    CATEGORY = (
        ("Historical", "Historical"),
        ("museums", "museums"),
        ("Forests", "Forests"),
        ("Public art","Public art"),
        ("national parks","national parks"),
    )
    title = models.CharField(max_length=102, blank=False,default='بدون عنوان')
    Description=models.TextField(default='بدون توضیحات', blank=False)
    Likes = models.CharField(max_length=1, blank=False, null=True,default='0')
    categories=models.CharField(max_length=200,blank=False,null=False,choices=CATEGORY,default=CATEGORY[1][1])
    Hardness=models.CharField(max_length=102, blank=False,default='بدون درجه ی سختی')
    Address=models.CharField(max_length=102, blank=False,default='بدون آدرس ')
    Time=models.CharField(max_length=102, blank=False,default='بدون  تخمین زمان ')
    City=models.CharField(max_length=102, blank=False,default='بدون شهر')
    Average=models.CharField(max_length=102, blank=False,default='0')
    
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class PlaceImage(models.Model): 
    places = models.ManyToManyField(Places)
    image = models.FileField(blank=True)
