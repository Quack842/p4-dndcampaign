from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm, CreateCampaignForm, BookForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db import models
from .models import Campaign, BookVenue
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import AuthenticationForm
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


def handler404(request, invalid_path):
    return render(request, '404.html', status=404)


class Home(generic.TemplateView):
    """ This will be the Home/Landing Page """
    template_name = "index.html"


class BookvenueList(generic.ListView):
    """
    This view is used to display all booking in the browse booking page
    """
    model = BookVenue
    queryset = BookVenue.objects.order_by('-booking_date')
    template_name = 'upcoming_campaigns.html'


# To create a new Campaign
class CreateCampaign(FormView, LoginRequiredMixin):
    """ This will be the Create Campaigns Page """
    template_name = "create_campaign.html"
    form_class = CreateCampaignForm
    success_url = '/dashboard/'

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


class Venue(FormView, LoginRequiredMixin):
    """ This will be the Venue Page """
    template_name = "venues.html"
    form_class = BookForm
    success_url = '/upcomingcampaigns/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Get the latest campaign
        latest_campaign = Campaign.objects.order_by('-created_on').first()
        # Set the latest campaign as the initial value for the campaigns field
        form.fields['campaigns'].initial = latest_campaign
        return form

    def form_valid(self, form):
        if form.is_valid():
            form = form.save(commit=False)
            form.user = User.objects.get(id=self.request.user.id)
            form.save()
            messages.success(self.request, "Successfully Registered to a Venue!")
            return super().form_valid(form)

        return HttpResponse(template.render(request, context))


class VenueList(generic.ListView):
    model = BookVenue
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
class DeleteCampaign(View, LoginRequiredMixin):
    def get(self, request, id):
        """ Get Campaign to be deleted and render a delete form """

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
        """ Delete existing Campaign """

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
class EditCampaign(View, LoginRequiredMixin):
    """ View to allow user to edit a specific Campaign"""

    def get(self, request, id):
        """ Get Campaign data and return a prefilled form """

        queryset = Campaign.objects.all()

        campaign = get_object_or_404(queryset, id=id)

        data = {'campaign_name': campaign.campaign_name,
                'dungeon_master': campaign.dungeon_master,
                'total_players': campaign.total_players,
                'description': campaign.description,
                }
        edit_form = CreateCampaignForm(initial=data)

        if campaign.user != request.user:
            # If the logged-in user is not the owner of the campaign,
            # redirect them to a suitable page or display an error message
            return HttpResponse("home")

        return render(
            request,
            'edit_campaign.html',
            {
                'campaign': campaign,
                'edit_form': edit_form
            }
        )

    def post(self, request, id):
        """
        Update existing Campaign using the form data
        """

        queryset = Campaign.objects.all()
        campaign = get_object_or_404(queryset, id=id)

        edit_form = CreateCampaignForm(instance=campaign, data=request.POST)
        if campaign.user != request.user:
            return HttpResponse("home")

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


# Delete Venue
class DeleteVenue(View, LoginRequiredMixin):
    def get(self, request, id):
        """ Get Venue to be deleted and render a delete form """

        queryset = BookVenue.objects.all()
        bookvenue = get_object_or_404(queryset, id=id)

        return render(
            request,
            'delete_venue.html',
            {
                'bookvenue': bookvenue,
            }
        )

    def post(self, request, id):
        """ Delete existing Venue """

        queryset = BookVenue.objects.all()
        bookvenue = get_object_or_404(queryset, id=id)

        bookvenue.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Your Venue has been deleted.'
        )

        return redirect("upcoming_campaigns")


# Edit Venue
class EditVenue(View, LoginRequiredMixin):
    """ View to allow user to edit a specific Venue"""

    def get(self, request, id):
        """ Get Venue data and return a prefilled form """

        queryset = BookVenue.objects.all()
        bookvenue = get_object_or_404(queryset, id=id)

        data = {'campaigns': bookvenue.campaigns,
                'venue': bookvenue.venue,
                'booking_date': bookvenue.booking_date,
                'booking_comments': bookvenue.booking_comments,
                }
        edit_form = BookForm(initial=data)

        if bookvenue.user != request.user:
            # If the logged-in user is not the owner of the venue,
            # redirect them to a suitable page or display an error message
            return HttpResponse("home")

        return render(
            request,
            'edit_venue.html',
            {
                'bookvenue': bookvenue,
                'edit_form': edit_form
            }
        )

    def post(self, request, id):
        """
        Update existing Venue using the form data
        """

        queryset = BookVenue.objects.all()
        bookvenue = get_object_or_404(queryset, id=id)

        edit_form = BookForm(instance=campaign, data=request.POST)

        if bookvenue.user != request.user:
            return HttpResponse("home")

        if edit_form.is_valid():
            bookvenue.campaigns = edit_form.cleaned_data.get(
                                     'campaigns')
            bookvenue.venue = edit_form.cleaned_data.get(
                                      'venue')
            bookvenue.booking_date = edit_form.cleaned_data.get(
                                     'booking_date')
            bookvenue.booking_comments = edit_form.cleaned_data.get(
                                   'booking_comments')
            bookvenue.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'You edited your Venue successfully.'
            )

        else:
            edit_form = BookForm()
            messages.add_message(
                request,
                messages.WARNING,
                'Your venue has not been edited.'
            )

        return redirect("upcoming_campaigns")
