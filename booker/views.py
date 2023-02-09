from django.shortcuts import render, redirect
from .forms import NewUserForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from django.http import HttpResponse
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


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


class Profile(generic.TemplateView):
    """ This will be the Profile Page """
    template_name = "account/profile.html"


def venue_view(request):
    context = {}
    form = RegionForm(request.GET)
    context['form'] = form
    if form.is_valid():
        messages.success(request, "Success")
        return redirect("venues")
    messages.error(request, "Error")
    return render(request, "venues.html", context)


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
                messages.info(request, f"You are now logged in as: {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="account/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You Have Successfully Logged Out!")
    return redirect("home")


# Update Profile Here
@login_required
def profile(request):
    if request.method == 'GET':
        p_form = ProfileUpdateForm(request.GET,
                                   request.FILES,
                                   instance=request.user.profile.image)
        if p_form.is_valid():
            p_form = p_form.save()
            messages.success(request, f'Your account has been updated!')
            # Redirect back to profile page
            return redirect('profile')
        else:
            messages.error(request, "Update was Unsuccessful")

    else:
        p_form = ProfileUpdateForm()

    context = {
        'p_form': p_form
    }

    return render(request, 'account/profile.html', context={"p_form": form})
