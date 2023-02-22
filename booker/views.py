from django.shortcuts import render, redirect, get_object_or_404
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
from django.views.generic.edit import FormView, DeleteView
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


class CampaignList(generic.ListView):
    model = Campaign
    queryset = Campaign.objects.order_by("-created_on")
    template_name = "dashboard.html"


class Dashboard(FormView):
    """ This will be the Dashboard Page """
    template_name = "dashboard.html"
    form_class = BookForm
    success_url = '/dashboard'

    def form_valid(self, form):
        if form.is_valid():
            form = form.save(commit=False)
            form.user = Campaign.objects.get(id=self.request.user.id)
            form.save()
            messages.success(self.request,
                             "Successfully Registered to a Venue!")
            return super().form_valid(form)

        return HttpResponse(template.render(request, context))


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


# Delete Campaign
class DeleteCampaign(View):
    def get(self, request, id):
        """ Get question to be deleted and render a delete form """

        queryset = Campaign.objects.all()
        campaign = get_object_or_404(queryset, id=id)

        return render(
            request,
            'delete_campaign.html',
            {
                'campaign': campaign,
            }
        )

    def post(self, request, id):
        """ Delete existing question """

        queryset = Campaign.objects.all()
        campaign = get_object_or_404(queryset, id=id)

        campaign.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Your campaign has been deleted.'
        )

        return redirect("dashboard")


# Edit Campaign
class EditCampaign(View):
    """ View to allow user to edit a specific question"""

    def get(self, request, id):
        """ Get question data and return a prefilled form """

        queryset = Campaign.objects.all()
        campaign = get_object_or_404(queryset, id=id)

        data = {'campaign_name': campaign.campaign_name,
                'dungeon_master': campaign.dungeon_master,
                'total_players': campaign.total_players,
                'description': campaign.description,
                }
        edit_form = CreateCampaignForm(initial=data)

        return render(
            request,
            'edit_campaign.html',
            {
                'campaign': campaign,
                'edit_form': edit_form
            }
        )

    def post(self, request, id):
        """ Update existing question using the form data
        and return to the home page
        """

        queryset = Campaign.objects.all()
        campaign = get_object_or_404(queryset, id=id)

        edit_form = CreateCampaignForm(instance=campaign, data=request.POST)

        if edit_form.is_valid():
            campaign.campaign_name = edit_form.cleaned_data.get(
                                     'campaign_name')
            campaign.dungeon_master = edit_form.cleaned_data.get(
                                      'dungeon_master')
            campaign.total_players = edit_form.cleaned_data.get(
                                     'total_players')
            campaign.description = edit_form.cleaned_data.get(
                                   'description')
            campaign.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'You edited your Campaign successfully.'
            )

        else:
            edit_form = CreateCampaignForm()
            messages.add_message(
                request,
                messages.WARNING,
                'Your question has not been edited.'
            )

        return redirect("dashboard")