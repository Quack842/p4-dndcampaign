from django.db import models
from django_flatpickr.widgets import DatePickerInput, DateTimePickerInput
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djchoices import DjangoChoices, ChoiceItem
from django.contrib.postgres.fields import ArrayField
from django.core.validators import ValidationError


class Campaign(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    campaign_name = models.CharField(max_length=150, unique=True,
                                     verbose_name="")
    dungeon_master = models.CharField(max_length=150,
                                      verbose_name="")
    total_players = models.IntegerField()
    discription = models.TextField(max_length=300, blank=True)

    # show how we want it to be displayed
    def __str__(self):
        return str(self.user)


class BookVenue(models.Model):
    # Region Options - Europe
    REGION_EUROPE = [
        ("Austria",
            (
                ("Kasematten - Schlossbergbühne", "Kasematten - Schlossbergbühne"),
                ("Bilderbox", "Bilderbox"),
            )),
        ("Germany",
            (
                ("Le Royal - The Event hall", "Le Royal - The Event hall"),
                ("Zapp Comics Games", "Zapp Comics Games"),
                ("Comic Room", "Comic Room"),
            )),
        ("France",
            (
                ("Len’s PC Gamer", "Len’s PC Gamer"),
                ("G.E.E.K.S", "G.E.E.K.S"),
                ("Librairie Comptoir de Reve", "Librairie Comptoir de Reve"),
            )),
        ("Italy",
            (
                ("Star Comic Store Napoli", "Star Comic Store Napoli"),
                ("Comix Green", "Comix Green"),
                ("Infinity Comics", "Infinity Comics"),
                ("Games & Geeks", "Games & Geeks"),
            )),
        ("Ireland",
            (
                ("Tyrrelstown House", "Tyrrelstown House"),
                ("Gloster House", "Gloster House"),
                ("Reroll Games", "Reroll Games"),
                ("The Gathering", "The Gathering"),
            )),
        ("Netherlands",
            (
                ("Purple Dragon", "Purple Dragon"),
                ("The Fantasy Realm", "The Fantasy Realm"),
                ("Arnhem", "Arnhem"),
                ("Warhammer", "Warhammer"),
            )),
        ("Spain",
            (
                ("Gremio De Dragones", "Gremio De Dragones"),
                ("Pulsar Store", "Pulsar Store"),
                ("Dungeon Marvels", "Dungeon Marvels"),
                ("Joc & Rol", "Joc & Rol"),
            )),
        ("United Kingtom (UK)",
            (
                ("Geek Retreat Blackburn", "Geek Retreat Blackburn"),
                ("4th Planet Games", "4th Planet Games"),
                ("Mutant Dice Games", "Mutant Dice Games"),
                ("Lancaster Board and Sword", "Lancaster Board and Sword"),
            )),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    venue = models.CharField(max_length=50, choices=REGION_EUROPE)
    booking_date = models.DateField(auto_now=False, unique=True)
    booking_comments = models.TextField(max_length=200, blank=True)

    # show how we want it to be displayed
    def __str__(self):
        return str(self.user)
