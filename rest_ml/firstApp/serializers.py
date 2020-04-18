from rest_framework import serializers
from firstApp import models

class PersonDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PersonDetail
        fields= ('first_name','last_name')

class MovieRatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.MovieRating
        fields= '__all__'