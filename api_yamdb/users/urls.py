from django.urls import path, include
from rest_framework import routers
from users.views import UserAdminViewSet, get_jwt_token, user_signup

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', UserAdminViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', user_signup, name='signup'),
    path('auth/token/', get_jwt_token, name='token')
]