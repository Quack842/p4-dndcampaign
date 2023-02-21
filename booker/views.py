from django.shortcuts import render, redirect
from .forms import NewUserForm, CreateCampaignForm, BookForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db import models
from .models import Campaign, BookVenue
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
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
    """
    This view is used to display all booking in the browse booing page
    """
    model = BookVenue
    queryset = BookVenue.objects.order_by('-booking_date')
    template_name = 'upcoming_campaigns.html'
    paginate_by = 8


# To create a new Campaign
class CreateCampaign(FormView):
    """ This will be the Create Campaigns Page """
    template_name = "create_campaign.html"
    form_class = CreateCampaignForm
    success_url = '/dashboard'

    def form_valid(self, form):
        if form.is_valid():
            campaign_name = form.cleaned_data.get('campaign_name')
            form = form.save(commit=False)
            form.user = User.objects.get(id=self.request.user.id)
            form.save()
            messages.success(self.request,
                             f"{campaign_name} was successfully Registered!")
            return super().form_valid(form)

        return HttpResponse(template.render(context, request))


class CreateCharacter(generic.TemplateView):
    """ This will be the Create Character Page """
    template_name = "create_character.html"


class CampaignList(generic.ListView):
    model = Campaign
    queryset = Campaign.objects.order_by("-created_on")
    template_name = "dashboard.html"


class Dashboard(View):
    """ This will be the Dashboard Page """
    form_class = BookForm
    success_url = '/dashboard'

    def form_valid(self, form):
        if form.is_valid():
            form = form.save(commit=False)
            form.user = User.objects.get(id=self.request.user.id)
            form.save()
            messages.success(self.request,
                             "Successfully Registered to a Venue!")
            return super().form_valid(form)

        # return HttpResponse(template.render(request, context))
        return render(
            request,
            "dashboard.html",
            {
                "user": user,
                "campaign_name": campaign_name,
                "dungeon_master": dungeon_master,
                "total_players": total_players,
                "discription": discription,
                "created_on": created_on
            },
        )


class Venue(generic.TemplateView):
    """ This will be the Venue Page """
    template_name = "venues.html"


class Profile(generic.TemplateView):
    """ This will be the Profile Page """
    template_name = "account/profile.html"


# To create a new User
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


# To Log into account
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


# To log out of account
def logout_request(request):
    """
    To Log out of the account form
    """
    logout(request)
    messages.info(request, "You Have Successfully Logged Out!")
    return redirect("home")


# Delete a campaign
class DeleteCampaign(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own recipes
    """
    model = Campaign
    template_name = 'delete_campaign.html'
    success_message = "Recipe deleted successfully"
    success_url = '/dashboard'

    def test_func(self):
        """
        Prevent another user from deleting other's recipes
        """
        campaign = self.get_object()
        return campaign.user == self.request.user

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display sucess message given
        SucessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteCampaign, self).delete(request, *args, **kwargs)
