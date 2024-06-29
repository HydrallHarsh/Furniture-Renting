from django.contrib.auth.models import User
from django.db import models


class Furniture(models.Model):
    owner = models.CharField(max_length=100)
    furniture_type = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    average_cost = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    minimum_rental_days = models.IntegerField()
    is_in_cart = models.BooleanField(
        default=False)  # New field for cart status

    def __str__(self):
        return self.furniture_type


# Create your models here.
# Example: models.py (Cart model)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Furniture, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
