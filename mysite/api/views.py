"""from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer


class BLogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer"""


from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to my Django app!")
