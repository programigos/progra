# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.template import loader
def login(request):
	template = loader.get_template('login.html')
	context = {}
	return HttpResponse(template.render(context,request))

# Create your views here.
