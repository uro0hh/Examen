from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.raw_product_list, name='lista_productos'),
    path('producto/<int:pk>/', views.product_detail, name='producto'),
    path('raw/', views.raw_product_list, name='raw_product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart_summary/', views.cart_summary, name='cart_summary'),
    path('search/', views.search_redirect, name='search_redirect'),

]
