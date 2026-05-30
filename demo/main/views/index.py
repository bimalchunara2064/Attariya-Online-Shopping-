from itertools import product

from django.shortcuts import render
from django.views import View
from main.models.category import Category
from main.models.products import Product

class IndexView(View):
    def get(self, request):
        hero_p1 = Product.objects.filter(product_featured='hero').order_by('?').first()
        promo_t1 =Product.objects.filter(product_featured='promo').order_by('?').first()
        categories=Category.objects.all().order_by('?')[:4]
        products = Product.objects.all().order_by('-id')[:30]
        trending=Product.objects.filter(product_featured='trending')
        best_sales= Product.objects.filter(product_featured='best_seller')
        featured_products= Product.objects.filter(product_featured='featured')
        default = Product.objects.filter(product_featured='default')

        context = {

            'products': products,
            'trendings': trending,
            'best_sales': best_sales,
            'featured_products':featured_products,
            'default': default,
            'hero_p1': hero_p1,
            'promo_t1': promo_t1,
            'categories': categories,
        }
        return render(request, 'index.html', context)
