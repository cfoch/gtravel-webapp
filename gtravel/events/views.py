from django.shortcuts import render_to_response
from django.template import RequestContext

from events.models import Event

def event_view(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render_to_response(
        "events/event.html",
        {'event': event},
        context_instance=RequestContext(request)
        )
