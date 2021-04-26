from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def product_list(request):
	products = Product.objects.all()
	context = {'products':products, 'title':'Список товаров'}
	
	return render(request, 'korzinka/product_list.html', context)


def product_details(request, product_id):
	product = Product.objects.get(id = product_id)
	context = {'product':product}
	return render(request, 'korzinka/product_details.html', context)