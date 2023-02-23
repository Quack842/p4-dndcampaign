from django.contrib import admin
from .models import Campaign, BookVenue
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Campaign)
class CampaignAdmin(SummernoteModelAdmin):

    list_display = ('user', 'campaign_name', 'dungeon_master', 'total_players',
                    'description', 'created_on')

    summernote_fields = ('description')


@admin.register(BookVenue)
class BookVenueAdmin(SummernoteModelAdmin):

    list_display = ('user', 'campaigns', 'venue', 'booking_date',
                    'booking_comments')

    summernote_fields = ('booking_comments')
