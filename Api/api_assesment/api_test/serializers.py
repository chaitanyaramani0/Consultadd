from rest_framework import serializers
from api_test.models import Books,Catagory,Author



class BookSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Books
        fields = ['name','price','discription','author','catagory','created']

class CatagorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Catagory
        fields = ['category']

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name','country']