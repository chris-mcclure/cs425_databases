from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Referee
# Create your views here.

def referees_list(request):
    referee_list = Referee.objects.all().order_by('id')
    context = {'referee_list': referee_list,}
    return render(request, 'referees/referees.html', context)

def referees_detail(request, slug):
	referee = Referee.objects.get(id=slug)
	context = {'referee': referee}
	return render(request, 'referees/referees_detail.html',context)
