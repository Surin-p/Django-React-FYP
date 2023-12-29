from django.shortcuts import render, HttpResponse
from .models import Student
# Create your views here.
def index(request):
    return HttpResponse("Hello,World")