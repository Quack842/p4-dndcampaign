from django.shortcuts import render, redirect
from .forms import NewUserForm, CreateCampaignForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db import models
from .models import Campaign
from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from cloudinary.forms import cl_init_js_callbacks
from django.views.generic.edit import FormView
from django.contrib.auth.models import User


class Home(generic.TemplateView):
    """ This will be the Home/Landing Page """
    template_name = "index.html"


class UpcomingCampaigns(generic.TemplateView):
    """ This will be the Upcomming Campaigns Page """
    template_name = "upcoming_campaigns.html"


class CreateCampaign(FormView):
    """ This will be the Create Campaigns Page """
    template_name = "create_campaign.html"
    form_class = CreateCampaignForm
    success_url = '/dashboard'
    campaign_loop = Campaign.objects.all()

    def form_valid(self, form):
        if form.is_valid():
            campaign_name = form.cleaned_data.get('campaign_name')
            form = form.save(commit=False)
            form.user = User.objects.get(id=self.request.user.id)
            form.save()
            messages.success(self.request, f"{campaign_name} was successfully Registered!")
            return super().form_valid(form)

        return HttpResponse(template.render(context, request))


class CreateCharacter(generic.TemplateView):
    """ This will be the Create Character Page """
    template_name = "create_character.html"


class Dashbaord(generic.TemplateView):
    """ This will be the Dashboard Page """
    template_name = "dashboard.html"


class Venue(generic.TemplateView):
    """ This will be the Venue Page """
    template_name = "venues.html"


class Profile(generic.TemplateView):
    """ This will be the Profile Page """
    template_name = "account/profile.html"


def register_request(request):
    """
    To create the Register Form
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Was Successful...")
            return redirect("home")
        messages.error(
            request, "Unsuccessful Registration. Invalid Information.")
    form = NewUserForm()
    return render(request=request, template_name="account/signup.html",
                  context={"register_form": form})


def login_request(request):
    """
    To Log into account form
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as: {username}")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="account/login.html",
                  context={"login_form": form})


def logout_request(request):
    """
    To Log out of the account form
    """
    logout(request)
    messages.info(request, "You Have Successfully Logged Out!")
    return redirect("home")


