from django.db import models

# Create your models here.

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

