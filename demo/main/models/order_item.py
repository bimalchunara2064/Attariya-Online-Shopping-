from django.db import models
from django.contrib.auth.models import User
from .products import Product
from .order import Order


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return self.order_id.order_id
