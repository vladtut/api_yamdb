from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import ReviewViewSet, CommentViewSet

# Создаётся роутер
# http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
# http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
                CommentViewSet, basename='comments', )
app_name = 'api'

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
