from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.managers_list, name="managers_list"),
	re_path(r'^(?P<slug>[\w]+)/$', views.managers_detail, name="managers_detail"),
]