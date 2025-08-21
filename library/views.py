from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BookSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

# class BookListApiView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers

class BookListApiView(APIView):
    def get(self,request):
        books = Books.objects.all()
        serializer_data = BookSerializers(books,many=True).data
        info = {
            'status':'Barcha kitoblar olib kelindi!',
            'books list':serializer_data
        }
        return Response(info, status=status.HTTP_200_OK)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers
#     lookup_field = 'id'

class BookDetailApiView(APIView):
    def get(self,request,pk):
        book = get_object_or_404(Books,pk=pk)
        serializer_data = BookSerializers(book).data
        info = {
            'status' : 'Book taken successfully',
            'book':serializer_data
        }
        return Response(info)

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers

class BookDeleteApiView(APIView):
    def delete(self,request,pk):
        try:
            book=Books.objects.get(id=pk)
            book.delete()
            return Response({'status' : 'This book deleted successfully'})
        except:
            return Response({'status' : "There isn't book like that!"})

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers

class BookUpdateApiView(APIView):
    def put(self,request,pk):
        book=get_object_or_404(Books,pk=pk)
        serializer = BookSerializers(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        try:
            book = Books.objects.get(id=pk)
            serializer = BookSerializers(book,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"There is error in your serializer"})


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers

class BookCreateApiView(APIView):
    def post(self, request):
        dataX = request.data
        serializer = BookSerializers(data=dataX)
        if serializer.is_valid():
            serializer.save()
            info = {
                'status' : 'This book is saved to Database',
                'book info' : dataX
            }
            return Response(info)

# class BookMixedApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers

class BookMixedApiView(APIView):
    def get(self,request,pk):
        book = get_object_or_404(Books,pk=pk)
        serializer_data = BookSerializers(book).data
        info = {
            'status' : 'About this book',
            'book':serializer_data
        }
        return Response(info)
    def delete(self,request,pk):
        try:
            book=Books.objects.get(id=pk)
            book.delete()
            return Response({'status' : 'This book deleted successfully'})
        except:
            return Response({'status' : "There isn't book like that!"})
    def put(self,request,pk):
        book=get_object_or_404(Books,pk=pk)
        serializer = BookSerializers(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        book = get_object_or_404(Books, pk=pk)
        serializer = BookSerializers(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)