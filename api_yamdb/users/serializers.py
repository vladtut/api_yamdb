from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('role',)
    
    def validate(self, attrs):
        email=attrs['email']
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {'email',}('Такой email уже используется')
            )
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create_user(validated_data)

class UserSignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
        required=True,
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate(self, attrs):
        email=attrs.get('email',)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email',}('Такой email уже используется')
            )
        return super().validate(attrs)

class UserSelfEditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        model = User
        read_only_fields = ('role',)

class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


