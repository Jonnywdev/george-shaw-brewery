from django.shortcuts import render

# Create your views here.


def cookie(request):
    """ A view to return the index page """

    return render(request, 'info/cookie.html')


def delivery(request):
    """ A view to return the index page """

    return render(request, 'info/delivery.html')


def privacy(request):
    """ A view to return the index page """

    return render(request, 'info/privacy.html')


def terms(request):
    """ A view to return the index page """

    return render(request, 'info/terms_and_conditions.html')