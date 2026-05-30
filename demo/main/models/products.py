from django.db import models
from main.models.category import Category

SELECTION = (
    ('promo', 'promo'),
    ('hero', 'Hero'),
    ('trending', 'Trending Product'),
    ('best_seller', 'Best selling Product'),
    ('featured', 'Featured Product'),
    ('default', ' Default Product'),
)


class Product(models.Model):
    name = models.CharField(max_length=300)
    thumbnails = models.ImageField(upload_to="products/")
    price = models.FloatField(default=0)
    old_price = models.FloatField(default=0, blank=True, null=True)
    qty = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    product_featured = models.CharField(max_length=300, choices=SELECTION, default='default')

    def __str__(self):
        return self.name


    def get_percentage(self):
        new_price = (self.old_price - self.price) / self.old_price * 100
        return new_price

    def get_save_amount(self):
        save_amount = (self.old_price - self.price)
        return save_amount
