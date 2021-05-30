from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

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
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        user_obj = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = UserSerializer(data=request.data)
    
    if (serializer.is_valid()):
        user = authenticate(
            request,
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        if user:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


