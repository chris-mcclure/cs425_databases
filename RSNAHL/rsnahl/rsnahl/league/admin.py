from django.contrib import admin
from .models import Person, Player, Team, Coach, Manager, Referee, Game
# Register your models here.

admin.site.register(Person)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Coach)
admin.site.register(Manager)
admin.site.register(Referee)
admin.site.register(Game)

