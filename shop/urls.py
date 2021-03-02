
from django.urls import path
from .views import ProductCreateView, cart


urlpatterns = [
    path('', ProductCreateView.as_view(), name='product_create'),
    path('cart/', cart, name='cart'),
]