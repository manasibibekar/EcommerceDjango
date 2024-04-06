from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def get_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}

    if request.GET.get('size'):
        size = request.GET.get('size')
        price = product.get_product_price_by_size(size)
        context['selected_size'] = size
        context['updated_price'] = price

    return render(request, 'products/product.html', context)