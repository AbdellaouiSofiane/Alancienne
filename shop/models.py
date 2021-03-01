from decimal import Decimal

from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
	TVA_CHOICES = [
		(None, 'Taux TVA'),
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

	def clean(self, *args, **kwargs):
		if self.stock_ordered > self.stock_available :
			raise ValidationError(
				{'stock_ordered' : 'Le stock commandé ne peut être\
									supérieur à la quantité maximum.'
				})
		else:
			super(Product, self).save(*args, **kwargs)



