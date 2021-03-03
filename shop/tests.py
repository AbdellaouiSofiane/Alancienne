from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import ProductCreateView, cart, cart_update_ajax, checkout
from .models import Product, Item, Cart
from decimal import Decimal

class test_url_list_is_resolved(SimpleTestCase):


	def test_product_create_resolves(self):
		url = reverse('product_create')
		self.assertEqual(resolve(url).func.view_class, ProductCreateView)

	def test_cart_resolves(self):
		url = reverse('cart')
		self.assertEqual(resolve(url).func, cart)

	def test_cart_update_resolves(self):
		url = reverse('cart_update')
		self.assertEqual(resolve(url).func, cart_update_ajax)

	def test_checkout_resolves(self):
		url = reverse('checkout')
		self.assertEqual(resolve(url).func, checkout)


class TestViews(TestCase):


	def setUp(self):
		self.client = Client()
		self.product_create = reverse('product_create')
		self.cart = reverse('cart')

	def test_product_create_GET(self):
		response = self.client.get(self.product_create)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'shop/product_create.html')

	def test_product_create_POST(self):
		response = self.client.post(self.product_create,{
			'name' : 'banane',
			'price' : Decimal('3.15'),
			'tva' : Decimal('0.055'),	
			'stock_available' : 20,
			'stock_ordered' : 5
		})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Product.objects.first().name, 'banane')

	def test_product_create_POST_invalid_quantity_ordered(self):
		response = self.client.post(self.product_create,{
			'name' : 'banane',
			'price' : Decimal('3.15'),
			'tva' : Decimal('0.055'),	
			'stock_available' : 20,
			'stock_ordered' : 21
		})
		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Product.objects.count(), 0)
		
	def test_cart_GET(self):
		response = self.client.get(self.cart)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'shop/cart.html')


	def test_cart_cookie(self):
		response = self.client.get(self.cart)
		session_id = self.client.session.session_key
		self.assertEqual(Cart.objects.get(id=1).session_id, session_id)

	

