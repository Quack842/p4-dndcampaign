from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views import generic, View


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


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Was Successful...")
            return redirect("home")
        messages.error(request, "Unsuccessful Registration. Invalid Information.")
    form = NewUserForm()
    return render(request=request, template_name="account/signup.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
                console.log("Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="account/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You Have Successfully Logged Out")
    return redirect("home")
