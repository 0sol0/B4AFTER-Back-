from rest_framework import serializers
from books.models import Book, Review, Image


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('book',)


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("content",)


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    likes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    top_ten = serializers.SerializerMethodField()
    def get_top_ten(self,obj):
        return obj.top_ten.url
    class Meta:
        model = Image
        fields = '__all__'