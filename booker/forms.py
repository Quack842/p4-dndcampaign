from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from .models import Profile


# Region Options - Europe
REGION_EUROPE = (
    ("1", "Austria"),
    ("2", "Germany"),
    ("3", "France"),
    ("4", "Italy"),
    ("5", "Ireland"),
    ("6", "Netherlands"),
    ("7", "United Kingdom (UK)"),
)

# Region Options - Europe - Austria
REGION_EUROPE_AUSTRIA = (
    ("1", "Kasematten - Schlossbergbühne"),
    ("2", "Bilderbox"),
)

# Region Options - Europe - Germany
REGION_EUROPE_GERMANY = (
    ("1", "Le Royal - The Event hall"),
    ("2", "Zapp Comics Games"),
    ("3", "Comic Room"),
)

# Region Options - Europe - France
REGION_EUROPE_FRANCE = (
    ("1", "Len’s PC Gamer"),
    ("2", "G.E.E.K.S"),
    ("3", "Librairie Comptoir de Reve"),
)

# Region Options - Europe - Italy
REGION_EUROPE_ITALY = (
    ("1", "Star Comic Store Napoli"),
    ("2", "Comix Green"),
    ("3", "Infinity Comics"),
    ("4", "Games & Geeks"),
)

# Region Options - Europe - Ireland
REGION_EUROPE_IRELAND = (
    ("1", "Tyrrelstown House"),
    ("2", "Gloster House"),
    ("3", "Reroll Games"),
    ("4", "The Gathering"),
)

# Region Options - Europe - Netherlands
REGION_EUROPE_NETHERLANDS = (
    ("1", "Purple Dragon"),
    ("2", "The Fantasy Realm"),
    ("3", "Arnhem"),
    ("4", "Warhammer"),
)

# Region Options - Europe - Spain
REGION_EUROPE_SPAIN = (
    ("1", "Gremio De Dragones"),
    ("2", "Pulsar Store"),
    ("3", "Dungeon Marvels"),
    ("4", "Joc & Rol"),
)

# Region Options - Europe - United Kingtom (UK)
REGION_EUROPE_UK = (
    ("1", "Geek Retreat Blackburn"),
    ("2", "4th Planet Games"),
    ("3", "Mutant Dice Games"),
    ("4", "Lancaster Board and Sword"),
)


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


# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']


# Form for Europe
class RegionForm(forms.Form):
    region_form_europe = forms.ChoiceField(choices=REGION_EUROPE)
    region_form_austria = forms.ChoiceField(choices=REGION_EUROPE_AUSTRIA)
    region_form_germany = forms.ChoiceField(choices=REGION_EUROPE_GERMANY)
    region_form_france = forms.ChoiceField(choices=REGION_EUROPE_FRANCE)
    region_form_italy = forms.ChoiceField(choices=REGION_EUROPE_ITALY)
    region_form_ireland = forms.ChoiceField(choices=REGION_EUROPE_IRELAND)
    region_form_netherlands = forms.ChoiceField(choices=REGION_EUROPE_NETHERLANDS)
    region_form_spain = forms.ChoiceField(choices=REGION_EUROPE_SPAIN)
    region_form_uk = forms.ChoiceField(choices=REGION_EUROPE_UK)
