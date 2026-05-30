from django.contrib import admin
from .models.products import Product
#from .models.users import User
from .models import Category
from .models.cart import Cart
from .models.shipping_address import ShippingAddress
from .models.order import Order
from .models.order_item import OrderItem
from .models.contact import Contact



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'product_featured')


admin.site.register(Product, ProductAdmin)
#admin.site.register(user)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Contact)

