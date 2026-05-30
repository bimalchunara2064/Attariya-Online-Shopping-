from django.shortcuts import render, redirect
from django.views import View
from main.models.order import Order
from main.models.shipping_address import ShippingAddress


class AccountsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            shipping_address = ShippingAddress.objects.get(user=request.user)
            orders = Order.objects.filter(user=request.user)
            sub_total = sum(orders.values_list('total_price', flat=True))
            shipping_price=0
            tax=0
            total_price = sub_total + shipping_price + tax

            context = {
                'orders': orders,
                'sub_total': sub_total,
                'shipping_price': shipping_price,
                'tax': tax,
                'total_price': total_price,
                'shipping_address': shipping_address,
            }
            return render(request, 'account.html', context)
        else:
            return redirect('login')
