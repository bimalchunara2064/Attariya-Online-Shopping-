
from django import views
from django.contrib import admin
from .views.index import IndexView
from django.urls import path
from .views.productDetail import ProductDetailView
from .views.cart import CartView,CartDeleteView
from .views.login import LoginView,LogoutView
from .views.checkout import CheckoutView
from .views.about import AboutView
from .views.category import CategoryView
from .views.register import RegisterView
from .views.account import AccountsView
from .views.contact import ContactView




urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('user/product_detail/<pid>/', ProductDetailView.as_view(), name='productDetail'),
    path('user/cart/', CartView.as_view(), name='cart'),
    path('user/cart/<cid>/', CartDeleteView.as_view(), name='cart_delete'),
    path('user/login/', LoginView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(), name='logout'),
    path('user/checkout/', CheckoutView.as_view(), name='checkout'),
    path('user/about/', AboutView.as_view(), name='about'),
    path('user/category/', CategoryView.as_view(), name='category'),
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/account/', AccountsView.as_view(), name='account'),
    path('user/contact/', ContactView.as_view(), name='contact'),

]
