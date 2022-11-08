from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

from users.serializers import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework.generics import get_object_or_404
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer,UserProfileSerializer #프로필 페이지
from .models import User


# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료"})
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated] # 로그인됐을 때만 할 수 있게.
    def get(self, request):
        print(request.user)
        user = request.user
        user.is_admin = True
        user.save()
        return Response("get 요청")

class ProfileView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer
        return Response(serializer.data)

