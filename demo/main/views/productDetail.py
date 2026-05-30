from django.shortcuts import render,redirect
from django.views import View
from main.models import Product
from main.models import cart
from main.models.cart import Cart


class ProductDetailView(View):
    def get(self, request, pid):
        product = Product.objects.get(id=pid)
        context = {
            'product': product,
        }
        return render(request, 'productDetail.html', context)

    def post(self, request, pid):
        if request.user.is_authenticated:
            product = Product.objects.get(id=pid)
            quantity = request.POST.get('quantity')
            cart_items = Cart.objects.filter(product=product,user=request.user).first()
            if cart_items:
                total_qty=int(cart_items.quantity)+int(quantity)
                cart_items.quantity=total_qty
                cart_items.total_price=product.price*int(quantity)
                cart_items.save()
            else:
                cart = Cart()
                cart.user = request.user
                cart.product = product
                cart.quantity = quantity
                cart.total_price = product.price * float(quantity)
                cart.save()

        return redirect('productDetail', pid)
