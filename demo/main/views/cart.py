from django.shortcuts import render, redirect
from django.views import View
from main.models.cart import Cart


class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            if cart:
                sub_total = sum(cart.values_list('total_price', flat=True))
                context = {
                    'cart': cart,
                    'sub_total': sub_total,
                }
                return render(request, 'cart.html', context)
            else:
                return redirect('index')
        else:
           return redirect('login')

    def post(self, request):
        qty = request.POST.get('quantity')
        cid = request.POST.get('cid')
        cart = Cart.objects.get(id=cid)
        cart.quantity = int(qty)
        cart.total_price = cart.product.price * float(qty)
        cart.save()
        #print(qty, cid)
        return redirect('cart')


class CartDeleteView(View):
    def get(self, request, cid):
        if request.user.is_authenticated:
            cart = Cart.objects.get(id=cid)
            if cart:
                cart.delete()
                return redirect('cart')
            else:
                return redirect('cart')

        else:
            return redirect('login')
