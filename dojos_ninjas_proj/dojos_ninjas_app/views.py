from django.shortcuts import render, redirect, HttpResponse
from .models import Dojo, Ninja

def index(request):
	# return HttpResponse('dojos_ninjas_proj / dojos_ninjas_app / views.index')
	context = {
		'title': 'Dojos & Ninjas',
		'dojos': Dojo.objects.all(),
		# 'ninjas': Ninja.objects.all().values()
	}
	if 'alert' in request.session and 'alert_message' in request.session:
		context['alert'] = request.session['alert']
		context['alert_message'] = request.session['alert_message']
	return render(request, 'index.html', context)

def add_dojo(request):
	# return HttpResponse('dojos_ninjas_proj / dojos_ninjas_app / views.add_ninja')
	dojo = Dojo(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
	dojos_filtered = Dojo.objects.filter(name__iexact=dojo.name, city__iexact=dojo.city, state__iexact=dojo.state)
	if len(dojos_filtered):
		request.session['alert'] = True
		request.session['alert_message'] = 'That dojo has already been added.'
	else:
		Dojo.objects.create(name=dojo.name, city=dojo.city, state=dojo.state)
	return redirect('/')

def add_ninja(request):
	# return HttpResponse('dojos_ninjas_proj / dojos_ninjas_app / views.add_ninja')
	dojo = Dojo.objects.get(id=int(request.POST['dojo']))
	ninja = Ninja(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=dojo)
	ninjas_filtered = Ninja.objects.filter(first_name__iexact=ninja.first_name, last_name__iexact=ninja.last_name, dojo_id=ninja.dojo.id)
	if len(ninjas_filtered):
		request.session['alert'] = True
		request.session['alert_message'] = 'That ninja has already been added.'
	else:
		Ninja.objects.create(first_name=ninja.first_name, last_name=ninja.last_name, dojo=ninja.dojo)
	return redirect('/')