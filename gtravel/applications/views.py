from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.db import IntegrityError
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test

from applications.models import Application
from events.models import Event
from applications.forms import ApplicationForm


@login_required
@user_passes_test(lambda u: u.groups.filter(name='applicant').count() > 0)
def manage_application(request, event_id):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        event = Event.objects.get(id=event_id)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.event = event
            instance.status = Application.MEMBERSHIP_STATUS_PENDING
            try:
                instance.save()
                form.save_m2m()
            except IntegrityError:
                # TODO: Handle this error.
                pass
            return HttpResponseRedirect("/events/%d/" % int(event_id))
    else:
        form = ApplicationForm()

    return render_to_response("application/application_form.html", 
        {"form": form}, context_instance=RequestContext(request))


class ApplicationDetailView(DetailView):

    model = Application
    template_name = "application_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        return context

