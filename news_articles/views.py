from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic
from django.contrib import messages
from .forms import NewsForm

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


def add_news_article(request):
    """ Add a news article """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry you do not have access to this part of the website.')
    #     return redirect(reverse('home'))

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            messages.success(request, f'You have successfully added!')
            return redirect(reverse('news'))
        else:
            messages.error(request, 'Failed to add an article. Please ensure the form is valid.')
    else:
        form = NewsForm()

    template = 'news/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
