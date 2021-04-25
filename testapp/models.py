from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    description=models.TextField()
    #storing book image
    picture=models.ImageField()
    # to store the bookprice
    price=models.FloatField()    
      
    #to display object in string format
    def __str__(self):
        return self.name
