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
        'User Detail': '/user/<str:pk>',
    }
    return Response(api_urls)

def getAllUsers(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


