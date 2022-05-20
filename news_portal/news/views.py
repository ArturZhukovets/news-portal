from django.shortcuts import render
from .models import NewsArticles
# Create your views here.


def news_home(request):
    news = NewsArticles.objects.order_by('-date')
    context = {'news': news}
    return render(request, 'news/news_home.html', context)


def news_create(request):
    return render(request, 'news/create.html')
