from django.urls import path,include 
from .views import book_list
from .views import *
urlpatterns = [
    path('', book_list, name='book_list'),  # Route for listing books
    path('add/', book_create, name='book_create'),  # Route for adding a book
    path('update/<int:id>/', book_update, name='book_update'),  # Route for updating a book
]