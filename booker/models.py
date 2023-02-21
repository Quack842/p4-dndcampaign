from django.db import models
from django_flatpickr.widgets import DatePickerInput, DateTimePickerInput
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djchoices import DjangoChoices, ChoiceItem
from django.contrib.postgres.fields import ArrayField
from django_summernote.widgets import SummernoteWidget
from django.core.validators import ValidationError
from django.utils import timezone


class Campaign(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="campaigns")
    campaign_name = models.CharField(max_length=150, unique=True,
                                     verbose_name="")
    dungeon_master = models.CharField(max_length=150,
                                      verbose_name="")
    total_players = models.IntegerField()
    discription = models.TextField(max_length=300, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    # show how we want it to be displayed
    def __str__(self):
        return str(self.user)


class BookVenue(models.Model):
    # Region Options - Europe
    REGION_EUROPE = [
        ("Austria",
            (
                ("Kasematten - Schlossbergbühne",
                 "Kasematten - Schlossbergbühne"),
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

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="venues")
    venue = models.CharField(max_length=50, choices=REGION_EUROPE)
    booking_date = models.DateField(auto_now=False)
    booking_comments = models.TextField(max_length=200, blank=True)

    class Meta:
        """To display the booking by booking_date descending order"""
        ordering = ['-booking_date']

    def get_absolute_url(self):
        """Get url after user adds/edits venue"""
        return reverse('upcoming_campaigns', kwargs={'slug': self.slug})

    # show how we want it to be displayed
    def __str__(self):
        return str(self.user)
