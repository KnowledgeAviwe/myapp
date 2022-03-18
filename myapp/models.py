from django.db import models

# Create your models here.
class FoodTable(models.Model):
    name = models.CharField(max_length=60)
    shop = models.CharField(max_length=60)
    orderDate= models.DateField()
    price = models.FloatField()

    def __str__(self):
        return self.name
