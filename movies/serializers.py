from rest_framework.serializers import *
from movies.models import *


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
