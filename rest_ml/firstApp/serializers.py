from rest_framework import serializers
from firstApp import models

class PersonDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PersonDetail
        fields= '__all__'