from django.shortcuts import render, HttpResponse, redirect
from .forms import AccountRegister
from django.contrib.auth import login, authenticate, logout
from .models import  Account
from django.contrib.auth.decorators import login_required


def account_login(request):
    template = 'account/user_login.html'
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('cart:product_list')
        else:
            return render(request, template, {'msg': 'Invalid Credentials.!'})
    context = {}
    return render(request, template, context)


def account_register(request):
    template = 'account/user_create.html'
    form = AccountRegister()
    if request.POST:
        form = AccountRegister(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            return redirect('account:account_login')
    
    context = {'form': form}
    return render(request, template, context)


@login_required(login_url='account:account_login')
def account_logout(request):
    logout(request)
    return redirect('account:account_login')



