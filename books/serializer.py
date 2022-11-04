from rest_framework import serializers
from books.models import Book, Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("title", "content")


class BookSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)
    interests = serializers.StringRelatedField(many=True)
    lives = serializers.StringRelatedField(many=True)

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Book
        fields = '__all__'


# class BookCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = '__all__'


# class BookListSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()
#     interests_count = serializers