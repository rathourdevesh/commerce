from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class itemDetails(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    bid = models.IntegerField()
    category = models.CharField(max_length=64,blank=True)
    Image = models.ImageField(upload_to='images/',blank=True)
    status = models.CharField(max_length=12,default="Active") 
    bidPrice = models.IntegerField(default=0)
    bidWinner = models.CharField(max_length=32,default='')
    time = models.DateTimeField()

    
class bidDetails(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(itemDetails,on_delete=models.CASCADE)
    amount = models.IntegerField()
    time = models.DateTimeField()

class comments(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(itemDetails,on_delete=models.CASCADE)
    Comment = models.CharField(max_length=512)
    time = models.DateTimeField()

class watchlist(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(itemDetails,on_delete=models.CASCADE,related_name="SelectItem")
    stat = models.CharField(max_length=12,default='')
