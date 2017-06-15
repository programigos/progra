from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.template import loader
from django.shortcuts import render
def index(request):
	template = loader.get_template('base.html')
	context = {}
	return HttpResponse(template.render(context,request))