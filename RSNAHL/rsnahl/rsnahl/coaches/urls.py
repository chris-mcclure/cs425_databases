from django.urls import path, re_path
from . import views


urlpatterns = [
	path('', views.coaches_list, name="coaches_list"),
	re_path(r'^(?P<slug>[\w]+)/$', views.coaches_detail, name="coaches_detail"),
]