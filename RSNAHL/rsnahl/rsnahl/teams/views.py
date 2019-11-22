from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Team
# Create your views here.

def teams(request):
    name_list = Team.objects.all().order_by('name')
    context = {'name_list': name_list,}
    return render(request, 'teams/teams.html', context)