from django.urls import path
from accounts.views import *
from products.views import *

urlpatterns = [
    path('login/', login_page, name='login_name'),
    path('register/', register_page, name='register_name'),
    path('activate/<email_token>/' , activate_email , name="activate_email"),
    path('add-to-cart/<uid>', add_to_cart, name='add_to_cart_name')
]