from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from unielv.models import *
# Create your views here.

def make_menu():
  group_list = []
  groups = Elevator.objects.all().values('group').distinct()

  for group in groups:
    elv_list = []

    g = group['group']
    elvs = Elevator.objects.filter(group=g).values('dong').distinct()

    for elv in elvs:
      elv_list.append((g, elv['dong']))

    group_list.append(elv_list)
  
  return group_list

def index(request):
  group_list = make_menu()

  return render(request, 'unielv/index.html', {'group_list': group_list})

def detail(request, elv_id):
  group_list = make_menu()
  elv_list = get_list_or_404(Elevator, dong = elv_id)

  context = {'elv_list': elv_list,
             'group_list': group_list}

  return render(request, 'unielv/detail.html', context)
