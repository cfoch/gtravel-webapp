from django.shortcuts import render

from applications.views import manage_application
from events.models import Event
#from applications.models import Application, PayPal, BankTransfer
from applications.forms import ApplicationForm

from utils import is_applicant

def event_view(request, event_id):
    event = Event.objects.get(pk=event_id)

    ctx = {
        'event': event
        }
    user = request.user
    if user.is_authenticated():
        application = Application.objects.filter(user=user,
            event=event_id)
        already_applied = application.count() > 0 #len == 1
        is_applicant_user = is_applicant(user)
        if is_applicant_user:
            if not already_applied:
                if request.method == 'POST':
                    form = ApplicationForm(request.POST)
                    if form.is_valid():
                        instance = form.save(commit=False)
                        instance.user = user
                        instance.event = event
                        instance.status = 0
                        instance.save()
                else:
                    form = ApplicationForm()
                ctx['form'] = form
            else:
                ctx['application'] = application[0]
        ctx['already_applied'] = already_applied
        ctx['is_applicant_user'] = is_applicant_user

    return render(request, 'events/event.html', ctx)

