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
from booker import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('upcomingcampaigns/', views.UpcomingCampaigns.as_view(), name='upcoming_campaigns'),
    path('createcampaigns/', views.CreateCampaign.as_view(), name='create_campaigns'),
    path('createcharacter/', views.CreateCharacter.as_view(), name='create_character'),
    path('dashboard/', views.Dashbaord.as_view(), name='dashboard'),
    path('venues/', views.Venue.as_view(), name='venues'),
    path('signup/', views.register_request, name="signup"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('profile/', views.Profile.as_view(), name="profile"),
]
