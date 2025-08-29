from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

# Create your views here.

def news_home(request):

    news = Articles.objects.all()

    return render(request, 'news_home/news_index.html', {'news' : news})

def create(request):

    error = ''
    if request.method == 'POST':
        form  = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Эээ баля, писать научись'

    form = ArticlesForm()

    data = {
        'form' : form,
        'error' : error
    }

    return render(request, 'news_home/news_create.html', data)