from django.urls import path

from .models import Training, Player
from .views import HomePageView, AddPlayerView, AddTraining, CategoryView, TrainingView, PlayerView

app_name = 'dochadzka_app'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('player/',AddPlayerView.as_view(), name='post'),
    path("training/<str:category_name>/",AddTraining.as_view(), name='training'),
    path("category/<str:category_name>/", CategoryView.as_view(), name="category"),
    path("training_view/<int:training_target>/<str:category_name>/'", TrainingView.as_view(), name="training_view"),
    path("player_view/<int:player_id>", PlayerView.as_view(), name='player_view'),
]