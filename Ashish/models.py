from django.db import models
from django.db import models

class Furniture(models.Model):
    owner = models.CharField(max_length=100)
    furniture_type = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    average_cost = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    minimum_rental_days = models.IntegerField()

    def __str__(self):
        return self.furniture_type

# Create your models here.
    