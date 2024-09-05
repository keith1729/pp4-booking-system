from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def AboutPage(request):
    return HttpResponse("This is the about page!")
