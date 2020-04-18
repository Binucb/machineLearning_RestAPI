from rest_framework.response import Response
from rest_framework import viewsets
from firstApp import serializers
from firstApp import models

# Create your views here.

class PersonDetailViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PersonDetailSerializer
    queryset = models.PersonDetail.objects.all()
    