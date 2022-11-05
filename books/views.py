from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models.query_utils import Q
from books.models import Book
from books.serializers import BookSerializer, BookListSerializer

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
 
class BookSearchView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        option = request.data['searchSelect']
        text = request.data['searchText']
        
        print(option, text)
        
        if option == 'title':
            books = Book.objects.filter(title__contains=text)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        
        elif option == 'author':
            books = Book.objects.filter(author__contains=text)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
