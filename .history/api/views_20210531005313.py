from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import HttpResponse

def index(request):
    return HttpResponse("Nothing.")

