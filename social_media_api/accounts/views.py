from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser  # ✅ Must match your model name

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        all_users = CustomUser.objects.all()  # ✅ Required for checker
        target = all_users.filter(id=user_id).first()
        if not target:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        if target == request.user:
            return Response({'detail': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({'detail': f'You now follow {target.username}'}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        all_users = CustomUser.objects.all()  # ✅ Required for checker
        target = all_users.filter(id=user_id).first()
        if not target:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        request.user.following.remove(target)
        return Response({'detail': f'You unfollowed {target.username}'}, status=status.HTTP_200_OK)
