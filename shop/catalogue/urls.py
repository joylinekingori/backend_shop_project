from django.urls import path
from .views import list_products
from .views import product_detail
urlpatterns=[
   path("products/", list_products, name="list_products"),
   path("products/<int:id>/", product_detail, name="product_details"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
   

   ]






