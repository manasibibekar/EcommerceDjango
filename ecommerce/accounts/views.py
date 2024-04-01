from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages


def login_page(request):
    return render(request, 'accounts/login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(
            username = email,
            first_name = first_name,
            last_name = last_name,
            email = email
        )
        user_obj.set_password(password)
        user_obj.save()

        messages.info(request, 'An email has been sent on your mail')
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'accounts/register.html')