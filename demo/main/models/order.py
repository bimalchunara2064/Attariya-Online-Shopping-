from django.db import models
from django.contrib.auth.models import User

ORDER_STATUS = {
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('ready to ship', 'Ready to ship'),
    ('shipped', 'Shipped'),
    ('canceled', 'Canceled'),
    ('paid', 'Paid'),
}

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
    total_price=models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(choices=ORDER_STATUS, default='pending', max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

    def get_order_items(self):
        from .order_item import OrderItem
        return OrderItem.objects.filter(order_id=self)

