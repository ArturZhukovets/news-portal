from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news-home'),
    path('create', views.news_create, name='create'),
    ]