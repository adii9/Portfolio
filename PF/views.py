from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    if 'GET':
        return HttpResponse('Hello World!!')
