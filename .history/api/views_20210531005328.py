from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view

def index(request):
    return HttpResponse("Nothing.")

