from django.shortcuts import render
from django.contrib import messages
from .models import News
# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def recent_news(request):
    """ A view to return the news on the index page """

    article = News.objects.all()

    context = {
        'article': article,
    }
