from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post
from django.views import generic
from django.contrib import messages
from .forms import NewsForm

# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "news/news.html"


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
            messages.success(request, f'You have successfully added "{article.title}"!')
            return redirect(reverse('article', args=[article.id]))
        else:
            messages.error(request, 'Failed to add an article. Please ensure the form is valid.')
    else:
        form = NewsForm()

    template = 'news/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_news_article(request, pk):
    """ Edit an article in the store """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry you do not have access to this part of the website.')
    #     return redirect(reverse('home'))

    article = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully updated "{article.title}"!')
            return redirect(reverse('article', args=[article.id]))
        else:
            messages.error(request, 'Failed to edit article. Please ensure the form is valid.')
    else:
        form = NewsForm(instance=article)
        messages.info(request, f'You are editing "{article.title}".')

    template = 'news/edit_article.html'
    context = {
        'form': form,
        'article': article,
    }

    return render(request, template, context)
