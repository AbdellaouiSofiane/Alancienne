from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin


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