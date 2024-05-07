from django.shortcuts import render
from rest_framework import generics
from api_test.serializers import BookSerializer,CatagorySerializer,AuthorSerializer
from api_test.models import Books,Catagory,Author

# Create your views here.


class BooksList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class CatagoryList(generics.ListCreateAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

class CatagoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer




    



