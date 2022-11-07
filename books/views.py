from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from django.db.models.query_utils import Q

from books.models import Book, Review
from books.serializer import ReviewSerializer, ReviewCreateSerializer, ReviewListSerializer, BookSerializer, BookListSerializer


class Book_List(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class BookListView(APIView):
#     def get(self, request, **kwargs):
#         category = request.GET.get('category')

#         if category == None:
#             query_set = Book.objects.all()
#         else:
#             query_set = Book.objects.filter(Q(category__contains=category))
#         book_serializer = BookSerializer(query_set, many=True)
#         return Response(book_serializer.data)


class Book_Detail(APIView):
    def get(self, request, isbn):
        book = get_object_or_404(Book, isbn=isbn)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Book_Review(APIView):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        reviews = book.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, book_id):
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, book_id=book_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Book_Review_Detail(APIView):
    def put(self, request, book_id, review_id):
        review = get_object_or_404(Review, id=book_id)
        if request.user == review.user:
            serializer =ReviewCreateSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, book_id, review_id):
        review = get_object_or_404(Review, id=book_id)
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)


class Review_List(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)







# class Books_Home(APIView):
#     def get(self, request):
#         get_top_ten_image()
#         image = Image()
#         image.top_ten = r'B4AFTER-Back-\books\static\most 10 book.png'
#         image.save()
#         image_serializer = ImageSerializer(image)

#         return Response(image_serializer.data)