from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djchoices import DjangoChoices, ChoiceItem
from django.contrib.postgres.fields import ArrayField


class Profile(models.Model):
    # Delete profile when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('profile_pics')

    # show how we want it to be displayed
    def __str__(self):
        return str(self.user)


class Campaign(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    campaign_name = models.CharField(max_length=150, unique=True)
    dungeon_master = models.CharField(max_length=150)
    total_players = models.IntegerField()
    discription = models.TextField(max_length=300, blank=True)


class BookVenue(models.Model):
    # Region Options - Europe
    REGION_EUROPE = [
        ("Austria",
            (
                ("1", "Kasematten - Schlossbergbühne"),
                ("2", "Bilderbox"),
            )),
        ("Germany",
            (
                ("1", "Le Royal - The Event hall"),
                ("2", "Zapp Comics Games"),
                ("3", "Comic Room"),
            )),
        ("France",
            (
                ("1", "Len’s PC Gamer"),
                ("2", "G.E.E.K.S"),
                ("3", "Librairie Comptoir de Reve"),
            )),
        ("Italy",
            (
                ("1", "Star Comic Store Napoli"),
                ("2", "Comix Green"),
                ("3", "Infinity Comics"),
                ("4", "Games & Geeks"),
            )),
        ("Ireland",
            (
                ("1", "Tyrrelstown House"),
                ("2", "Gloster House"),
                ("3", "Reroll Games"),
                ("4", "The Gathering"),
            )),
        ("Netherlands",
            (
                ("1", "Purple Dragon"),
                ("2", "The Fantasy Realm"),
                ("3", "Arnhem"),
                ("4", "Warhammer"),
            )),
        ("Spain",
            (
                ("1", "Gremio De Dragones"),
                ("2", "Pulsar Store"),
                ("3", "Dungeon Marvels"),
                ("4", "Joc & Rol"),
            )),
        ("United Kingtom (UK)",
            (
                ("1", "Geek Retreat Blackburn"),
                ("2", "4th Planet Games"),
                ("3", "Mutant Dice Games"),
                ("4", "Lancaster Board and Sword"),
            )),
    ]

    booking_id = models.UUIDField(primary_key=True, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings")
    venue = models.CharField(max_length=50, choices=REGION_EUROPE)
    booking_date = models.DateField(auto_now=False)
    booking_comments = models.TextField(max_length=200, blank=True)
    total_players = models.IntegerField()

    class Meta:
        ordering = ['-booking_date']
