from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect
from django.template import RequestContext

from applications.models import Application
from events.models import Event

from applications.forms import ApplicationForm

def manage_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            #FIXME 
            instance.event = Event.objects.get(pk=1)
            instance.status = 0 #pending
            instance.save()
    else:
        form = ApplicationForm()
    return render_to_response("applications/application_form.html", 
        {"form": form},
        context_instance=RequestContext(request)
        )

