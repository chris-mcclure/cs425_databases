from django.urls import path, re_path
from . import views


urlpatterns = [
	path('', views.teams_list, name="team_list"),
	re_path(r'^(?P<slug>[\w]+)/$', views.teams_detail, name="team_detail"),

]