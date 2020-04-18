from django.urls import path,include
from rest_framework.routers import DefaultRouter

from firstApp import views

router = DefaultRouter()
router.register('person',views.PersonDetailViewSet)
router.register('movie',views.MovieRatingViewSet)

urlpatterns = [
    path('',include(router.urls)),
]