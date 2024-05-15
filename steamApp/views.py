import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from steamApp.forms import ProductForm


# Create your views here.


def createProducts(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.creatorUser = request.user
            product.save()
            return redirect('home')
        else:
            # El formulario no es válido, devuelve una respuesta JSON con los errores del formulario
            print(form.errors)
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)  # Bad request status code


    else:
        form = ProductForm()
    context = {'form': form}

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
