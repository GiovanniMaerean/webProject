import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from steamApp.forms import ProductForm


# Create your views here.


def createProducts(request):
    form = ProductForm(request.POST)
    context = {'form': form}

    if form.is_valid():
        product = form.save(commit=False)
        product.creatorUser = request.user
        product.save()
        return redirect('home')

    return render(request, 'createProduct.html', context)


def get_steam_app_list(request):
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)


def get_steam_app_details(request, app_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)
