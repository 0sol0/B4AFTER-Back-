from django.urls import path
from books import views

urlpatterns = [
    # path('', views.Books_Home.as_view(), name='books_home'),
    path('explore/', views.BookListView.as_view(), name='book_list_view'),
    path('explore/<str:isbn>/', views.Book_Detail.as_view(), name='book_detail'),
    path('explore/<str:isbn>/favorites/', views.FavoritView.as_view(), name='favorit_view'),
    path('explore/<str:isbn>/review/', views.Book_Review.as_view(), name='book_review'),
    path('explore/<str:isbn>/review/<int:review_id>/', views.Book_Review_Detail.as_view(), name='book_review_detail'),
    path('search/', views.BookSearchView.as_view(), name='book_search_view'),
]