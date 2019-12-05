from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.players_list, name="players_list"),
	re_path(r'^(?P<slug>[\w]+)/$', views.players_detail, name="players_detail"),
	# path('', views.coaches_list, name="coaches_list"),
	# re_path(r'^(?P<slug>[\w]+)/$', views.coaches_detail, name="coaches_detail"),
]