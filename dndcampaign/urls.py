"""dndcampaign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from booker import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('upcomingcampaigns/', views.UpcomingCampaigns.as_view(),
         name='upcoming_campaigns'),
    path('createcampaign/', views.CreateCampaign.as_view(),
         name='create_campaign'),
    path('createcharacter/', views.CreateCharacter.as_view(),
         name='create_character'),
    path('dashboard/', views.CampaignList.as_view(), name='dashboard'),
    path('campaign/<slug:slug>/delete/', views.DeleteCampaign.as_view(),
         name='delete_campaign'),
    path('venues/', views.Venue.as_view(), name='venues'),
    path('signup/', views.register_request, name="signup"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('createcampaign/', views.CreateCampaign.as_view(),
         name="createcampaign"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('summernote/', include('django_summernote.urls')),
]
