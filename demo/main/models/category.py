from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category/', default='category/default.jpg')

    def __str__(self):
        return self.name
