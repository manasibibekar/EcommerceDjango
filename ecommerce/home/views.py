from django.shortcuts import render
from products.models import *

def index(request):
    context = {'products': Product.objects.all()}
    return render(request, 'home/index.html', context)