from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def index(request):

    context_dict = {}

    return render(request, 'main/home.html', context=context_dict)
