from django.shortcuts import render

# Create your views here.


def refund(request):
    """ A view to return the index page """

    return render(request, 'info/refund.html')


def delivery(request):
    """ A view to return the index page """

    return render(request, 'info/delivery.html')


def privacy(request):
    """ A view to return the index page """

    return render(request, 'info/privacy.html')


def terms(request):
    """ A view to return the index page """

    return render(request, 'info/terms_and_conditions.html')