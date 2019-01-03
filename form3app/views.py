# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from form3app.models import Cost
from form3app.form import CostForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.


	
	
def costView(request):
	if request.method == 'POST': #if the form has been submitted...
	# COntactForm was defined in the previous section
	
		form = CostForm(request.POST) #a form bound to the POST data
		if form.is_valid(): #all validation rules pass
			date = request.POST.get('date', '') #.get will return no error if 'date is not filled'
			cost = request.POST.get('cost', '') #.get will return no error if 'date is not filled'
			cost_obj = Cost(date = date,cost = cost) #get the data into the Cost model
			cost_obj.save() #save data into database
			
			
			return HttpResponseRedirect(reverse('form3app:cost')) #redirect after POST
	else:
		form = CostForm() #An unbound form
		
		
		template_name='jobs/cost.html'
		posts = list(Cost.objects.all())
		for e in Cost.objects.all():
			print(e.cost,e.date)
			
		args = {'form': form, 'posts': posts}
		return render(request, template_name, args)
		
		#return render(request, 'jobs/cost.html', {
		#'form':form,
		
		#})