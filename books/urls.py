from django.urls import path
from books import views

urlpatterns = [
    path('home/', views.Books_Home.as_view(), name='books_home'),
    path('search/', views.BookSearchView.as_view(), name='book_search_view'),
    path('<str:book_id>/', views.Book_Detail.as_view(), name='bookdetail'),
    path('<str:book_id>/review/', views.Book_Review.as_view(), name='bookreview'),
    path('<str:book_id>/review/<int:review_id>/', views.Book_Review_Detail.as_view(), name='book_review_detail'),
]
