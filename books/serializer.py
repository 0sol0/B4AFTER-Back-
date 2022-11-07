from rest_framework import serializers
from books.models import Book, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('book',)


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("content",)


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'