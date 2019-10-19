from django.db import models

# Create your models here.

class Places(models.Model):
    Title=models.CharField(max_length=500)
    Image=models.ImageField(upload_to="E:\SE_Project_DjangoRest98/photos",null=True,blank=False)
    Description=models.TextField()
    
    def __unicode__(self):
        return self.Title

    def __str__(self):
        return self.Title