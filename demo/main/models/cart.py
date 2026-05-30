from django.db import models
from .products import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.product.name