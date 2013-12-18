from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from userprofile.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print "Is valid"
            form.save()
    else:
        form = SignUpForm()
    return render_to_response("home/signup.html", 
        {"form": form},
        context_instance=RequestContext(request)
        )

