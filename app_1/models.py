from django.db import models

# Create your models here.
class blogpost(models.Model):
    title   = models.CharField(max_length=120,default = "Title ")
    content = models.TextField(default = "Content ")
    author  = models.CharField(max_length=120, default="Author name")
    date    = models.DateField()
    
class shopProduct(models.Model):
    title   = models.CharField(max_length=120,default = "Product Title ")
    description = models.TextField(default = "Product Description")
    price  = models.CharField(max_length=120, default="00.00") 
    img=models.ImageField(upload_to='images/') 

   
    
