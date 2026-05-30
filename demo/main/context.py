from main.models.cart import Cart


def default(request):
    try:
        cart = Cart.objects.filter(user=request.user)
    except:
        cart = 0

    return {
        'cart': cart,
    }
