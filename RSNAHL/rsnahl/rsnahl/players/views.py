from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Player
# Create your views here.

def players_list(request):
    name_list = Player.objects.all().order_by('id')
    context = {'name_list': name_list,}
    return render(request, 'players/players.html', context)

def players_detail(request, slug):
	player = Player.objects.get(id=slug)
	context = {'player': player}
	return render(request, 'players/player_detail.html',context)