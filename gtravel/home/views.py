from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from home.forms import LoginForm

from events.models import Event
from datetime import date

def index(request):
    upcoming_events = Event.objects.filter(
        start_date__gt=date.today()
        ).order_by('start_date')
    return render_to_response("home/index.html",
        {"events": upcoming_events},
        context_instance=RequestContext(request)
        )

def login_view(request):
    message = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                else:
                    message = "User and/or passwordd invalid"
        form = LoginForm()
        ctx = {'form': form, 'message': message}
        return render_to_response('home/login.html', ctx,
            context_instance=RequestContext(request))
        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home/')

