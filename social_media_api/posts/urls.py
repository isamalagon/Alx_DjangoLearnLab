from django.urls import path, include
from .views import FeedView
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),



]
