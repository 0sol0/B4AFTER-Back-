from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.query_utils import Q

from books.book_recommend import *
from books.models import Book, Review, Image
from books.serializer import ReviewSerializer, ReviewCreateSerializer, BookSerializer, BookListSerializer, ImageSerializer



# 전체 보기(List)
class BookListView(APIView):
    def get(self, request, **kwargs):
        category = request.GET.get('category')

        if category == None:
            query_set = Book.objects.all()
        else:
            query_set = Book.objects.filter(Q(category__contains=category))
        book_serializer = BookListSerializer(query_set, many=True)
        return Response(book_serializer.data)




# 홈 페이지
class Books_Home(APIView):
    def get(self, request):
        result = get_top_ten_image()
        top_ten_list = result["book_title"].tolist()
        print(top_ten_list)
        
        image = Image()
        image.top_ten = r'books\static\most_10_book.png'
        image.save()
        image_serializer = ImageSerializer(image)

        return Response(image_serializer.data)

# 검색
class BookSearchView(APIView):
    def get(self, request, **kwargs):
        searchSelect = request.GET.get('searchSelect')
        searchText = request.GET.get('searchText')

        if searchText == None:
            query_set = Book.objects.all()
        else:
            if searchSelect == 'book_title':
                query_set = Book.objects.filter(Q(book_title__contains=searchText))
            elif searchSelect == 'book_author':
                query_set = Book.objects.filter(Q(book_author__contains=searchText))
        book_serializer = BookSerializer(query_set, many=True)
        return Response(book_serializer.data)

# 상세 보기
class Book_Detail(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# 리뷰 보기/등록
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


# 리뷰 수정/삭제
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



class FavoritView(APIView):
    def post(self, request, isbn):
        books = get_object_or_404(Book, isbn=isbn)
        if request.user in books.favorites.all():
            books.favorites.remove(request.user)
            return Response('관심 목록에서 삭제했습니다', status=status.HTTP_200_OK)
        else:
            books.favorites.add(request.user)
            return Response('관심 목록에 추가 했습니다', status=status.HTTP_200_OK)
        








