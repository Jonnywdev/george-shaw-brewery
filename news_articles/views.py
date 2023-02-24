from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic
# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "news/news.html"
    paginate_by = 6


def article(request, pk):
    article = get_object_or_404(Post, id=pk)

    context = {'article': article, }
    return render(request, 'news/full_article.html', context)
