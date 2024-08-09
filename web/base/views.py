from django.shortcuts import render

# Create your views here.

def landing(request):
    context = {}
    response = render(request, 'base/index.html', context)
    return response