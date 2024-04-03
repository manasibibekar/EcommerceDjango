from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def get_product(request, slug):
    context = {'product': get_object_or_404(Product, slug=slug)}
    return render(request, 'products/product.html', context)