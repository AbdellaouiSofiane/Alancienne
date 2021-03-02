
from django.urls import path
from .views import ProductCreateView, cart, cart_update_ajax


urlpatterns = [
    path('', ProductCreateView.as_view(), name='product_create'),
    path('cart/', cart, name='cart'),
    path('cart_update/', cart_update_ajax, name='cart_update'),
]