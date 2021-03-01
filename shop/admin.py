from django.contrib import admin
from .models import Product, Item, Cart



class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'tva', 'price_ttc',
					'stock_available', 'stock_ordered', 
				    'stock_left']


class ItemAdmin(admin.ModelAdmin):
	list_display = [ 'cart', 'product', 'quantity']


class CartAdmin(admin.ModelAdmin):
	list_display = [ 'session_id', 'checked_out']


admin.site.register(Product, ProductAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Cart, CartAdmin)