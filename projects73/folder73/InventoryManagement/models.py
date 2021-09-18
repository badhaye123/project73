from django.db import models

# Create your models here.
class Product(models.Model):
    Date = models.DateField()
    Provider = models.CharField(max_length=30)
    Name_of_product = models.CharField(max_length=30)
    Price = models.IntegerField()
    Quality = models.IntegerField()
    Amount = models.IntegerField()
    Stock = models.IntegerField()
    
    
    def __str__(self):
        return self.Name_of_product 


