from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View

# Create your views here.


class Home(generic.TemplateView):
    """ This will be the Home/Landing Page """
    template_name = "index.html"
