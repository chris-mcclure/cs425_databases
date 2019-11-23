from django.urls import path, re_path
from . import views


urlpatterns = [
	path('', views.games_list, name="game_list"),
	re_path(r'^(?P<slug>[\w]+)/$', views.games_detail, name="game_detail"),
]