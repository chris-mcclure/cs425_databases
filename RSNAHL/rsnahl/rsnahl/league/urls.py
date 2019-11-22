from django.urls import path, re_path
from . import views

urlpatterns = [
	path('teams/', views.teams, name="teams_list"),
	re_path(r'^teams/(?P<slug>[\w-]+)/$', views.team_detail, name="team_detail"),
	path('players/', views.players),
]