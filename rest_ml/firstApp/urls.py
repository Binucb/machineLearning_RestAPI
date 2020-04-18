from django.urls import path,include
from rest_framework.routers import DefaultRouter

from firstApp import views

router = DefaultRouter()
router.register('person',views.PersonDetailViewSet)

urlpatterns = [
    path('',include(router.urls)),
]