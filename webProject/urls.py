"""
URL configuration for webProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

from steamApp import views
from steamApp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("createProducts/", views.createProducts, name="createProducts"),
    path('get-steam-app-list/', get_steam_app_list, name='get_steam_app_list'),
    path('get-steam-app-details/<int:app_id>/', get_steam_app_details, name='get_steam_app_details'),
    path('showProducts/', showProducts, name='showProducts'),
    path('deleteProduct/<uuid:id>/', deleteProduct, name='deleteProduct'),
    path('search/', search, {'inputValue': ""}, name='search'),
    path('search/<str:inputValue>/', search, name='search'),
    path('detailedSearch/<int:app_id>/', detailedSearch, name='detailedSearch'),
    path('modifyProduct/<uuid:id>/', modifyProduct, name='modifyProduct'),
    path('createDevelopers/', createDeveloper, name='createDeveloper'),
    path('showDevelopers/', showDevelopers, name='showDevelopers'),
    path('createPublisher/', createPublisher, name='createPublisher'),
    path('showPublishers/', showPublishers, name='showPublishers'),
    path('createSteamUser/', createSteamUser, name='createSteamUser'),
    path('showSteamUsers/', showSteamUsers, name='showSteamUsers'),
    path('deletePublisher/<uuid:id>/', deletePublisher, name='deletePublisher'),
    path('deleteDeveloper/<uuid:id>/', deleteDeveloper, name='deleteDeveloper'),
    path('deleteSteamUser/<uuid:id>/', deleteSteamUser, name='deleteSteamUser'),
    path('modifyDeveloper/<uuid:id>/', modifyDeveloper, name='modifyDeveloper'),
    path('modifyPublisher/<uuid:id>/', modifyPublisher, name='modifyPublisher'),
    path('modifySteamUser/<uuid:id>/', modifySteamUser, name='modifySteamUser'),
    path('productDetails/<uuid:id>/', productDetails, name='productDetails'),
    path('publisherDetails/<uuid:id>/', publisherDetails, name='publisherDetails'),
    path('developerDetails/<uuid:id>/', developerDetails, name='developerDetails'),
    path('steamUserDetails/<uuid:id>/', steamUserDetails, name='steamUserDetails'),

]
