from rest_framework import serializers
from reviews.models import Category, Genre, Title, Comment, Review, User
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        lookup_field = 'slug'
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        lookup_field = 'slug'
        model = Genre


class TitlesSerializer(serializers.ModelSerializer):
    """Основной метод записи информации."""
    category = serializers.SlugRelatedField(
        slug_field='slug', many=False, queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        required=False,
        queryset=Genre.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Title


class TitlesViewSerializer(serializers.ModelSerializer):
    """Основной метод просмотра информации."""
    category = CategorySerializer(many=False, required=True)
    genre = GenreSerializer(many=True, required=False)
    rating = serializers.IntegerField()

    class Meta:
        fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category'
        )
        model = Title
        read_only_fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category'
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Review

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        #title_id = self.context['view'].kwargs.get("title_id")
        #raise ValidationError("Вы не можите подписаться на самого себя.")
        return data

    def validate_score(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError(
                "Оценка должна быть целым числом от 1 до 10")
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role',)


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

    def validate_username(self, value):
        if value.lower() == 'me':
            raise serializers.ValidationError(
                'me - последняя буква в алфавите')
        return value

    class Meta:
        fields = ('username', 'email',)
        model = User


class UserSelfEditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role',)
        model = User
        read_only_fields = ('role',)


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()
