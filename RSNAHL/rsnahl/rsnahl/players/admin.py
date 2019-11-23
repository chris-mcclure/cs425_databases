from django.contrib import admin
from . models import Player, Coach, Manager, Referee

# Register your models here.
admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(Manager)
admin.site.register(Referee)
