from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    api_urls = {
        'register': '/auth/register/',
        'login': '/auth/login/',
        
    }
    return Response("Nothing.")

