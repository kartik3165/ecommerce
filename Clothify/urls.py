from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth', views.auth, name='auth'),

    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login'),
    path('logout', views.sign_out, name='logout'),

    path('cart', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add-to-cart'),
    path('delete-cart-item/<int:product_id>', views.delete_cart_item, name='delete-cart-item'),

    path('checkout', views.checkout, name='checkout'),
    path('orders', views.orders, name='orders'),

    path('product-details/<int:id>', views.product_details, name='product-deatils'),
    path('product-list', views.product_list, name='product-list'),
    path('category-product-list/<str:category>', views.category_product_list, name='category-product-list'),
    

]