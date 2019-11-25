from django.db import models
from Places.models import Places
from Users.models import Leader,User

# Create your models here.
class TravelLouge(models.Model):
    title = models.CharField(max_length=102, blank=False,default='بدون موضوع')
    description=models.TextField(default='بدون توضیح', blank=False)
    image1=models.ImageField(upload_to='image/%Y/%m/%d/',blank=True)
    image2=models.ImageField(upload_to='image/%Y/%m/%d/',blank=True)
    image3=models.ImageField(upload_to='image/%Y/%m/%d/',blank=True)
    leader=models.ForeignKey(Leader,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    places=models.ForeignKey(Places,on_delete=models.CASCADE)  
