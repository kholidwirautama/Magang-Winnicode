from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.permissions import IsAuthenticated

from cat.models import *
from subcat.models import *
from newsletter.models import *
from news.models import *
from contactform.models import *
from comment.models import *

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

# Subcategory ViewSet
class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCat.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [permissions.AllowAny]

# Newsletter ViewSet
class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.AllowAny]

# News ViewSet
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(act=1).order_by('-date', '-time')
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = News.objects.filter(act=1)
        ocatid = self.request.query_params.get('ocatid')
        name = self.request.query_params.get('name')
        if ocatid:
            queryset = queryset.filter(ocatid=ocatid)
        if name:
            queryset = queryset.filter(name=name)
        return queryset


# Contact Form ViewSet
class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.AllowAny]

# Comments ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

# HOME
class LastNews2View(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        news = News.objects.filter(act=1).order_by('-date', '-time')[:4]
        return Response(NewsSerializer(news, many=True).data)

class PopularNewsView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        news = News.objects.filter(act=1, show__gt=0).order_by('-show')[:10]
        return Response(NewsSerializer(news, many=True).data)

# NEWS DETAIL
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)