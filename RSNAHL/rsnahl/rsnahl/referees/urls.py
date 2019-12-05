from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.referees_list, name="referees_list"),
	re_path(r'^(?P<slug>[\w]+)/$', views.referees_detail, name="referees_detail"),
]