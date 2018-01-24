from django.shortcuts import render
from parse.models import Page, User
from backend.core import cache

def show (request):
    results = Page.objects.all()
    # user = User.objects.first()
    return render(request, 'index.html', {'notes':results})

def add(request):
    url = request.POST.get('url')
    cache.addCache(url)


def delete(request):
    id = request.POST.get('id')
    cache.deleteCache(id)
    results = Page.objects.all()
    # user = User.objects.first()
    return render(request, 'index.html', {'notes': results})

