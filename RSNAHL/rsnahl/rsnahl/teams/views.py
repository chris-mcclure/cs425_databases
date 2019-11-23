from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Team
# Create your views here.

def teams_list(request):
    name_list = Team.objects.all().order_by('name')
    context = {'name_list': name_list,}
    return render(request, 'teams/teams.html', context)

def teams_detail(request, slug):
	team = Team.objects.get(slug=slug)
	context = {'team': team}
	return render(request, 'teams/team_detail.html',context)
