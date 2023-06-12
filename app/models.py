from django.db import models

# Create your models here.


class Product_category(models.Model):
    PCname=models.CharField(max_length=50)
    PCid=models.IntegerField()
    
class Product(models.Model):
    PCid=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=100)
    Pprice=models.IntegerField()
    Pdecription=models.CharField(max_length=100)
    Pdate=models.DateField()