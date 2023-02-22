from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import RecentNews
# Create your views here.


def news_article(request):
    """ A view to show all news articles """

    newsarticles = RecentNews.objects.all()

    template = 'news/news.html'
    context = {
        'newsarticles': newsarticles,
    }
    return render(request, template, context)
