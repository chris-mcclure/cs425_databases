from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Game
# Create your views here.

def games_list(request):
    game_list = Game.objects.all().order_by('date')
    context = {'game_list': game_list,}
    return render(request, 'games/games.html', context)

def games_detail(request, slug):
	game = Game.objects.get(id=slug)
	context = {'game': game}
	return render(request, 'games/game_detail.html',context)
