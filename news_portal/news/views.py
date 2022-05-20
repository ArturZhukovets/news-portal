from django.shortcuts import render, redirect
from .models import NewsArticles
from .forms import NewArticlesForm

# Create your views here.


def news_home(request):
    news = NewsArticles.objects.order_by('-date')
    context = {'news': news}
    return render(request, 'news/news_home.html', context)


def news_create(request):
    """ creating a connection with ArticlesForm and Articles Model
    Data processing from the form will take place at 'news_create' url"""
    error = ''    # text for error if form is not valid
    if request.method == 'POST':
        form = NewArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news-home')
        else:
            error = "Form was incorrect"
    form = NewArticlesForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', context)
