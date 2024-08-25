# from django.urls import path,include 
# from .views import *
# urlpatterns = [
#     path('', author_list, name='book_list'),  # Route for listing books
#     path('add/', author_create, name='book_create'),  # Route for adding a book
#     path('update/<int:id>/', author_update, name='author_update'), 
#     path('delete/<int:id>', author_delete, name='author_delete'),
#   ]
from django.urls import path
from .views import *
urlpatterns=[
    path('',author_list,name='author_list'),
    path('Add/',author_create,name='author_create'),
    path('update/<int:id>',author_update,name='author_update'),
    path('delete/<int:id>',author_delete,name='author_delete'),
    path('<int:id>',author_show,name='author_show')

]