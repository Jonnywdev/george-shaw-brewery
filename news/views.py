from django.shortcuts import render
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
