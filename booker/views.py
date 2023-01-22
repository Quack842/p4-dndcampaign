from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View

# Create your views here.


class Home(generic.TemplateView):
    """ This will be the Home/Landing Page """
    template_name = "index.html"


class UpcomingCampaigns(generic.TemplateView):
    """ This will be the Upcomming Campaigns Page """
    template_name = "upcoming_campaigns.html"


class CreateCampaign(generic.TemplateView):
    """ This will be the Create Campaigns Page """
    template_name = "create_campaigns.html"


class CreateCharacter(generic.TemplateView):
    """ This will be the Create Character Page """
    template_name = "create_character.html"


class Dashbaord(generic.TemplateView):
    """ This will be the Dashboard Page """
    template_name = "dashboard.html"


class Venue(generic.TemplateView):
    """ This will be the Venue Page """
    template_name = "venues.html"
