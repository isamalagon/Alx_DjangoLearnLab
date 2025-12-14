from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import User



# Create your views here.
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = User.objects.filter(id=user_id).first()
        if not target:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        if target == request.user:
            return Response({'detail': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({'detail': f'You now follow {target.username}'}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = User.objects.filter(id=user_id).first()
        if not target:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        request.user.following.remove(target)

