from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/', login_page, name='login_name'),
    path('register/', register_page, name='register_name'),
    path('activate/<email_token>/' , activate_email , name="activate_email"),
]