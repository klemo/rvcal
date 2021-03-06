from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from forms import ShiftForm
from models import Shift
import datetime

def index(request):
  context = {}
  if request.method == 'POST': # If the form has been submitted...
    form = ShiftForm(request.POST) # A form bound to the POST data
    context['form'] = form
    if form.is_valid():             
      return HttpResponseRedirect('/thanks/')
  else:
    form = ShiftForm()
    context['form'] = form

  template = 'index.html'
  return render_to_response(template, context)

def events(request):
  events = []
  shifts = Shift.objects.all()
  for shift in shifts:
  	events.append({ 'title': shift.person.username, 'start':
  	              shift.date.isoformat() })
  return HttpResponse(simplejson.dumps(events), mimetype="text/plain")
