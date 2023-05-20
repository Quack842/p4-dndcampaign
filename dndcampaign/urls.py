from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from booker import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render


urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('upcomingcampaigns/', views.BookvenueList.as_view(),
         name='upcoming_campaigns'),
    path('createcampaign/', login_required(views.CreateCampaign.as_view()),
         name='create_campaign'),
    path('dashboard/', views.CampaignList.as_view(), name='dashboard'),
    path('venues/', views.Venue.as_view(), name='venues'),
    path('signup/', views.register_request, name="signup"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('summernote/', include('django_summernote.urls')),
    path(
        'delete_campaign/<int:id>/',
        login_required(views.DeleteCampaign.as_view()),
        name='delete_campaign'
    ),
    path(
        'edit_campaign/<int:id>/',
        login_required(views.EditCampaign.as_view()),
        name='edit_campaign'
    ),
    path(
        'delete_venue/<int:id>/',
        login_required(views.DeleteVenue.as_view()),
        name='delete_venue'
    ),
    path(
        'edit_venue/<int:id>/',
        login_required(views.EditVenue.as_view()),
        name='edit_venue'
    ),
    path('<path:invalid_path>', views.handler404),  # Catch all invalid URLs
]

handler404 = 'booker.views.handler404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
