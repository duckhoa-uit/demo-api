from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import CustomUser

@api_view(['GET'])
def index(request):
    api_urls = {
        'Register': '/auth/register/',
        'Login': '/auth/login/',
        'All Users': '/users/',
        'User Detail': '/users/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def getAllUsers(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    
    if (serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)


