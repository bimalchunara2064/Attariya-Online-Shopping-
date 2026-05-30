from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from main.models.cart import Cart
from main.models.shipping_address import ShippingAddress
from main.form import ShippingAddressForm
from main.models.order import Order
from main.models.order_item import OrderItem
import random


class CheckoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            shipping_address = ShippingAddress.objects.filter(user=request.user).first()
            form = ShippingAddressForm(instance=shipping_address)
            cart = Cart.objects.filter(user=request.user)
            if cart:
                sub_total = sum(cart.values_list('total_price', flat=True))
                context = {
                    'cart': cart,
                    'sub_total': sub_total,
                    'form': form,
                    'shipping_address': shipping_address,
                }
                return render(request, 'checkout.html', context)
            else:
                return redirect('index')
        else:
            return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            cart = (Cart.objects.filter(user=request.user))
            total = sum(cart.values_list('total_price', flat=True))
            shipping_address = ShippingAddress.objects.filter(user=request.user).first()
            form = ShippingAddressForm(request.POST, instance=shipping_address)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.save()
                order_id = "qr" + str(random.randint(100000, 999999))
                order = Order()
                order.user = request.user
                order.order_id = order_id
                order.total_price = total
                order.save()

                for item in cart:
                    order_item = OrderItem()
                    order_item.user = request.user
                    order_item.product = item.product
                    order_item.quantity = item.quantity
                    order_item.total_price = item.total_price
                    order_item.order_id = order
                    order_item.save()
                    item.delete()

                return render(request, 'success.html', {'order_id': order_id})
            else:
                return redirect('checkout')

        else:
            return redirect('login')
