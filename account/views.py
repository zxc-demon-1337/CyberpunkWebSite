# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, ImageForm
from django.contrib.auth import logout
from .models import Image
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'account/my_account.html')

def register(request):
    error = ''

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('homepage')
        else:
            error = "писать научись, чучело"
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form, 'error':error})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

def add_product(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.user = request.user
            form1.save()
            return redirect('homepage')
        else:
            print(form.errors)
    else:
        form = ImageForm()

    return render(request, 'account/add_product.html', {'form' :form})


@login_required
def my_products(request):
    form = Image.objects.filter(user=request.user)
    return render(request, 'account/my_products.html', {'form' : form })

