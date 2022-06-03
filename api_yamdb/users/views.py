from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import UserSerializer, UserSignUpSerializer, UserSelfEditSerializer, TokenSerializer
from .models import User
from rest_framework import permissions
from .permissions import IsAdmin
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.tokens import AccessToken
from django.core.mail import send_mail
from rest_framework.decorators import action

class UserAdminViewSet(viewsets.ModelViewSet): # создаем класс наследник viewset
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    lookup_field = 'username'


    @action(detail=False, url_path='me', methods=['get', 'patch'], permission_classes=[permissions.IsAuthenticated], serializer_class=UserSelfEditSerializer)
    def me(self, request):
        user=self.request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user, many=False)
            return Response(serializer.data)
        if request.method == 'PATCH':
            serializer = UserSelfEditSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_signup(request):
    serializer = UserSignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='Регистрация',
        message=f'Ваш код: {confirmation_code}',
        from_email=None,
        recipient_list=[user.email],
    )
    return Response(serializer.data, status=status.HTTP_200_OK)

    
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    if default_token_generator.check_token(
        user, serializer.validated_data['confirmation_code']
    ):
        token = AccessToken.for_user(user)
        return Response({'token': str(token)}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
