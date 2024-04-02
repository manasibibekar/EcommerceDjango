from django.urls import path
from .views import *

urlpatterns = [
    path('<slug>/' , get_product , name="get_product"),
]