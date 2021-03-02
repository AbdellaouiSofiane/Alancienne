from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from .models import Product, Item, Cart
from .forms import ProductCreateForm


class ProductCreateView(SuccessMessageMixin, CreateView):
	form_class = ProductCreateForm
	model = Product
	template_name = 'shop/product_create.html'
	success_url = reverse_lazy('product_create')
	success_message = "Le produit a été ajouter avec succès"


def cart(request):
	if not request.session.exists(request.session.session_key):
   		request.session.create() 
	cart, created = Cart.objects.get_or_create(
						session_id=request.session.session_key,
						checked_out=False)
	if created:
		for product in Product.objects.all():
			Item.objects.create(cart=cart, product=product)
	return render(request, 'shop/cart.html', {'cart': cart})


def cart_update_ajax(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			item = Item.objects.get(id=request.POST['item_id'])
		except ObjectDoesNotExist :
			return JsonResponse({'error': 'No such item exists in the database'})
		item.quantity = request.POST.get('item_quantity', 0)
		item.save()
		response = {
			'total_price' : item.cart.total_ttc(),
			'total_quantity' : item.cart.total_quantity()
		}
		return JsonResponse(response, status=200)
	else :
		return JsonResponse({'error': 'Failed'})


def checkout(request):
	cart = Cart.objects.get(
						session_id=request.session.session_key,
						checked_out=False)
	if cart.total_ttc() > 0:
		for item in cart.items.all():
			item.product.stock_ordered += item.quantity
			item.product.save()
		cart.checked_out = True
		cart.save()
		request.session.flush()
		messages.success(request, 'Votre panier a été commandé.')
	else:
		messages.warning(request, 'Votre panier est vide, merci de selectionner la quantité désirée.')

	return redirect('cart')