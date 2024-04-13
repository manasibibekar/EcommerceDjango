from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from accounts.models import *


def get_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}

    if request.GET.get('size'):
        size = request.GET.get('size')
        price = product.get_product_price_by_size(size)
        context['selected_size'] = size
        context['updated_price'] = price

    return render(request, 'products/product.html', context)


def add_to_cart(request, product_uid):
    product = Product.objects.get(uid=product_uid)
    user = request.user

    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    
    cart_item = CartItems.objects.create(cart=cart, product=product)

    size_variant_name = request.GET.get('size')
    if size_variant_name:
        size_variant = SizeVariant.objects.get(size_name=size_variant_name)
        cart_item.size_variant = size_variant
        cart_item.save()
    
    return HttpResponseRedirect(request.path_info)