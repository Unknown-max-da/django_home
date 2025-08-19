from django.shortcuts import render
from rest_framework import generics
from .models import Books
from serializers import BookSerializers
# Create your views here.

class BookListApiView(generics.ListAPIView):
    queryset = Books
    serializer_class = BookSerializers

class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'id'

class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializers
