from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    data = {
        'title' : 'penes bl`yad`',
        'array' : ['8==D', 'zalypa', 1488]
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, "main/about.html")

def test(request):
    return render(request, "main/test.html")

@login_required(login_url='/account/login/')
def account(request):
    return render(request, 'account/my_account.html')
