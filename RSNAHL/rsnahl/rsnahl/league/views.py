from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Team, Player, Coach, Manager, Person
# Create your views here.

def teams(request):
    name_list = Team.objects.all().order_by('name') 
    context = {'name_list': name_list,}
    return render(request, 'leagues/teams.html', context)

def team_detail(request, slug):
	return HttpResponse(slug)

def players(request):
    name_list = Player.objects.all().order_by('id')
    context = {'name_list': name_list,}
    return render(request, 'leagues/players.html', context)

# def coaches(request):
#     name_list = Person.objects.order_by('number')
#     context = {'name_list': name_list,}
#     return render(request, 'pages/players.html', context)

# def managers(request):
#     name_list = Player.objects.order_by('number')
#     context = {'name_list': name_list,}
#     return render(request, 'pages/players.html', context)

# def games(request):
#     team
#     context = {'name_list': name_list,}
#     return render(request, 'pages/players.html', context)