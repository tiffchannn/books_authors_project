from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('books/<int:book_id>', views.displayBook),
    path('addAuthorToBook', views.addAuthorToBook),
    path('addBookToAuthor', views.addBookToAuthor),
    path('authors/<int:author_id>', views.displayAuthor),
    path('authors', views.author),
    path('addAuthor', views.addAuthor)
]