from django.urls import path

from .models import Training
from.views import HomePageView, AddPlayerView, AddTraining, CategoryView

app_name = 'dochadzka_app'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('player/',AddPlayerView.as_view(), name='post'),
    path('training/',AddTraining.as_view(), name='training'),
    path('category/', CategoryView.as_view(), name='category'),
]