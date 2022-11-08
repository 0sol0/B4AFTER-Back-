from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import User
from books.serializer import BookListSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data) # DB에 전달됨
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, validated_data):
        user = super().create(validated_data) # DB에 전달됨
        password = user.password
        user.set_password(password) # 해싱
        user.save() # 저장
        return user





class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email # 커스터마이징

        return token


#user profile에 들어갈 관심도서 리스트
class UserProfileSerializer(serializers.ModelSerializer):
    bookmarks = BookListSerializer(many=True) #Books App의 serializers.py와 연결

    class Meta:
        model = User
        fields = ("email", "title", "content", "created_at", "updated_at", "like", "comment", "bookmarks", "like")