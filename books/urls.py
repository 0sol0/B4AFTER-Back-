from django.urls import path
from books import views

urlpatterns = [
    path('', views.Books_Home.as_view(), name='books_home'),
    path('<int:book_id>/', views.Book_Detail.as_view(), name='bookdetail'),
    path('<int:book_id>/review/', views.Book_Review.as_view(), name='bookreview'),
    path('<int:book_id>/review/<int:review_id>/', views.Book_Review_Detail.as_view(), name='book_review_detail'),
    path('<int:book_id>/', views.Book_Interest.as_view(), name='book_interest'),
    path('<int:book_id>/', views.Book_Life.as_view(), name='book_life'),
]