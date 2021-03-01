from django.shortcuts import render
from .models import Product
from django.views.generic import CreateView
from .forms import ProductCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy



class ProductCreateView(SuccessMessageMixin, CreateView):
	form_class = ProductCreateForm
	model = Product
	template_name = 'shop/product_create.html'
	success_url = reverse_lazy('product_create')
	success_message = "Le produit a été ajouter avec succès"