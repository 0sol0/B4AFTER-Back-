from django.urls import path
from books.views import BookListView, BookSearchView

urlpatterns = [
    path('explore/', BookListView.as_view(), name='book_list_view'),
    path('search/', BookSearchView.as_view(), name='book_list_view'),
]
