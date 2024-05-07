from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api_test.views import BooksDetail,BooksList,CatagoryList,CatagoryDetail,AuthorList,AuthorDetail


urlpatterns = [
    path('books/', BooksList.as_view()),
    path('books/<int:pk>/', BooksDetail.as_view()),
    path('catagory/', CatagoryList.as_view()),
    path('catagory/<int:pk>/', CatagoryDetail.as_view()),
    path('author/', AuthorList.as_view()),
    path('author/<int:pk>/', AuthorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)