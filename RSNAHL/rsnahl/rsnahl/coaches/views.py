from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Coach
# Create your views here.

def coaches_list(request):
    coach_list = Coach.objects.all().order_by('id')
    context = {'coach_list': coach_list,}
    return render(request, 'coaches/coaches.html', context)

def coaches_detail(request, slug):
	coach = Coach.objects.get(id=slug)
	context = {'coach': coach}
	return render(request, 'coaches/coaches_detail.html',context)
