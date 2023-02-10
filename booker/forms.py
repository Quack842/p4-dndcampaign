from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from .models import Profile, BookVenue, Campaign


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name",)
        ("phone_number", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user


class BookForm(forms.ModelForm):

    class Meta:
        model = BookVenue

        fields = (
            'venue',
            'booking_date',
            'booking_comments',
            'total_players',
        )


class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign

        fields = (
            'campaign_name',
            'dungeon_master',
            'total_players',
            'discription',
        )


# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Create a ProfileUpdateForm to update image.
class PhotoForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
