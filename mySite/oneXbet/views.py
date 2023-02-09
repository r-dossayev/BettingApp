from django.http import HttpResponseNotFound
from django.shortcuts import render


# Create your views here.

def handler404(request, exception):
    return render(request, '404page.html', status=404)


def handler500(request, exception):
    return render(request, '404page.html', status=500)


def index(request):
    return render(request, 'index.html')
