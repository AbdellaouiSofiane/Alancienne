from decimal import Decimal

from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
	TVA_CHOICES = [
		(Decimal('0.05'), '5,5 %'),
		(Decimal('0.2'), '20 %')
	]
	name = models.CharField(verbose_name='nom', 
							max_length=100)
	price = models.DecimalField(verbose_name='prix', 
								max_digits=5, 
								decimal_places=2)
	tva = models.DecimalField(verbose_name='tva', 
							  choices=TVA_CHOICES, 
							  max_digits=3, 
							  decimal_places=2)
	stock_available = models.PositiveIntegerField(
								verbose_name='stock disponible')
	stock_ordered = models.PositiveIntegerField(
								verbose_name='stock commandé')

	def __str__(self):
		return self.name

	def price_ttc(self):
		return round(self.price * (1 + self.tva), 2)

	def stock_left(self):
		return self.stock_available - self.stock_ordered

	def get_choices_list(self):
		return range(0, self.stock_available - self.stock_ordered + 1)

	def clean(self, *args, **kwargs):
		if self.stock_ordered > self.stock_available :
			raise ValidationError(
				{'stock_ordered' : 'Le stock commandé ne peut être\
									supérieur à la quantité maximum.'
				})
		else:
			super(Product, self).save(*args, **kwargs)



class Cart(models.Model):
	session_id = models.CharField(max_length=250)
	checked_out = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)

	def total_ttc(self):
		return sum([item.product.price_ttc() *  item.quantity for item in self.items.all()])

	def total_quantity(self):
		return sum([item.quantity for item in self.items.all()])
	

class Item(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f'{self.product} x {self.quantity}'

	def clean(self, *args, **kwargs):
		if self.quantity > self.product.stock_left():
			raise ValidationError({'quantity':'Stock insuffisant.'})
		else:
			super(Item, self).save(*args, **kwargs)