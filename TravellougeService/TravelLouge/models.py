from django.db import models
from Places.models import Places
from Users.models import Leader,user

# Create your models here.
class TravelLouge(models.Model):
    auther=models.ForeignKey(user,on_delete=models.CASCADE)
    title = models.CharField(max_length=102)
    description=models.CharField(max_length=1000)
    image1=models.ImageField(upload_to='image/%Y/%m/%d/',default='travellouge/defualt.jpg')
    image2=models.ImageField(upload_to='image/%Y/%m/%d/',default='travellouge/defualt.jpg')
    image3=models.ImageField(upload_to='image/%Y/%m/%d/',default='travellouge/defualt.jpg')
    places=models.ManyToManyField(Places)  
