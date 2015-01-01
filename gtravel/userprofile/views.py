from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from userprofile.forms import SignUpForm
from home.forms import LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('/login/') # signup?
    else:
        form = SignUpForm()
    return render_to_response("home/signup.html", 
        {"form": form},
        context_instance=RequestContext(request)
        )

