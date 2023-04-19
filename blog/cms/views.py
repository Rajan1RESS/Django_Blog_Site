from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework import filters
# from django.contrib.auth.models import User

from .models import Author, Blog, Country
from .serializers import AuthorSerializer,BlogSerializer,CountrySerializer
# ,UserSerializer


# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class AuthorViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
    search_fields = ['name','surname','languages_name']


class CountryViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Country.objects.all().order_by('id')
    serializer_class = CountrySerializer

class BlogViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer
