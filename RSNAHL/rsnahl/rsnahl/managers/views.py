from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Manager
# Create your views here.

def managers_list(request):
    manager_list = Manager.objects.all().order_by('id')
    context = {'manager_list': manager_list,}
    return render(request, 'managers/managers.html', context)

def managers_detail(request, slug):
	manager = Manager.objects.get(id=slug)
	context = {'manager': manager}
	return render(request, 'managers/managers_detail.html',context)
