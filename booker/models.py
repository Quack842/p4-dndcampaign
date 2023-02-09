from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djchoices import DjangoChoices, ChoiceItem
from django.contrib.postgres.fields import ArrayField


# Region Options - Europe
REGION_EUROPE = (
    ("Austria", "Austria"),
    ("Germany", "Germany"),
    ("France", "France"),
    ("Italy", "Italy"),
    ("Ireland", "Ireland"),
    ("Netherlands", "Netherlands"),
    ("United Kingdom (UK)", "United Kingdom (UK)"),
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


class Profile(models.Model):
    # Delete profile when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')

    # show how we want it to be displayed
    def __str__(self):
        return f'{self.user.username}'


# Form for Europe
class RegionForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region_form_europe = models.CharField(choices=REGION_EUROPE, max_length=300)
    if region_form_europe == "Austria":
        region_form_austria = models.CharField(choices=REGION_EUROPE_AUSTRIA, max_length=300)
    elif region_form_europe == "Germany":
        region_form_germany = models.CharField(choices=REGION_EUROPE_GERMANY, max_length=300)