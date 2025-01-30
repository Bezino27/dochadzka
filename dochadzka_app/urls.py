from django.urls import path
from.views import HomePageView, AddPlayerView

app_name = 'dochadzka_app'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('post/',AddPlayerView.as_view(), name='post'),
]