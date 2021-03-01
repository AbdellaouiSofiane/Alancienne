from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'tva', 'price_ttc',
					'stock_available', 'stock_ordered', 
				    'stock_left']


admin.site.register(Product, ProductAdmin)