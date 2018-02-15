from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
'''function based view'''


def home(request):
    # return HttpResponse('hello')
    base_var = 'szwarc'
    return render(request, "base.html", {'base_var': base_var})  # response
