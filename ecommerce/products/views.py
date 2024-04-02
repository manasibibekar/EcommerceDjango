from django.shortcuts import render

def get_product(request, slug):
    return render(request, 'products/product.html')