from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Select
from django_flatpickr.widgets import DatePickerInput, DateTimePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from .models import BookVenue, Campaign


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name",)
        ("password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class BookForm(forms.ModelForm):

    class Meta:
        model = BookVenue

        fields = (
            'venue',
            'campaigns',
            'booking_date',
            'booking_comments',
        )

        widgets = {
            'venue': Select(attrs={
                'class': 'form-control',
            }),
            'campaigns': Select(attrs={
                'class': 'form-control',
            }),
            'booking_date': DatePickerInput(attrs={
                'class': "form-control",
                }),
            'booking_comments': SummernoteWidget()
        }

    def save(self, commit=False):
        user = super(BookForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class CreateCampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign

        fields = (
            'campaign_name',
            'dungeon_master',
            'total_players',
            'description',
        )

        widgets = {
            'campaign_name': TextInput(attrs={
                'class': "form-control campaign-styling-left",
                'placeholder': 'Campaign Name',
                }),
            'dungeon_master': TextInput(attrs={
                'class': "form-control campaign-styling-left",
                'placeholder': 'Dungeon Master',
                }),
            'total_players': NumberInput(attrs={
                'class': "form-control campaign-styling-int",
                'max': 8.0,
                'min': 3.0,
                'text-align': 'center'
                }),
            'description': SummernoteWidget(),
        }

    def save(self, commit=False):
        user = super(CreateCampaignForm, self).save(commit=False)
        if commit:
            user.save()
        return user
