from django.shortcuts import render
from .models import RecentNews
# Create your views here.


def news(request):
    context = {

    }
    return render(request, 'news/news.html', context)