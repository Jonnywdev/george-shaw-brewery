from django.shortcuts import render

# Create your views here.


def our_story(request):
    """ A view to return the our story page """

    return render(request, 'our_story/our_story.html')