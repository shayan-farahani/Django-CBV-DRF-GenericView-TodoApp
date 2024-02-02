from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, "auth/index.html")    

