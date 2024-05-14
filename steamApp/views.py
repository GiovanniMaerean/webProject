import requests
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.


def createProducts(request):
    return render(request, 'createProduct.html')


def get_steam_app_list(request):
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)
