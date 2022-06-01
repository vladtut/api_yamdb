from rest_framework import serializers

from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        lookup_field = 'slug'
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        lookup_field = 'slug'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        slug_field='slug',
        many=False,
        queryset=Category.objects.all(),
        required=False
    )
    genre = GenreSerializer(
        slug_field='slug',
        many=True,
        required=False,
        queryset=Genre.objects.all()
    )
    rating = serializers.IntegerField()

    class Meta:
        fields = '__all__'
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