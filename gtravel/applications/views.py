from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect
from django.template import RequestContext

from applications.models import Application
from events.models import Event

from applications.forms import ApplicationForm


#@user_passes_test(lambda u: u.groups.filter(name='applicant').count() > 0)
def manage_application(request, event):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            #FIXME 
            instance.event = event
            instance.status = 0 #pending
            instance.save()
    else:
        form = ApplicationForm()

    return render_to_response("applications/application_form.html", 
        {"form": form},
        context_instance=RequestContext(request)
        )

