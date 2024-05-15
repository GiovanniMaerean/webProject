import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from steamApp.forms import ProductForm
from steamApp.models import Product


# Create your views here.


@csrf_exempt
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


def showProducts(request):
    products = Product.objects.filter(creatorUser=request.user)
    context = {'products': products}
    return render(request, 'showProduct.html', context)


def deleteProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('showProducts')


def search(request):
    search_value = None
    products = []

    if request.method == 'POST':
        search_value = request.POST.get('inputValue').lower()
        # Realizar la solicitud a la API de Steam para obtener la lista de productos
        response = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')

        if response.status_code == 200:
            app_list = response.json()['applist']['apps']
            # Filtrar la lista de productos para obtener aquellos que comienzan con el valor de búsqueda
            products = [{'appid': app['appid'], 'name': app['name']} for app in app_list if app['name'].lower().startswith(search_value)]

            products.sort(key=lambda x: x['name'].lower())

    return render(request, 'search.html', {'search_value': search_value, 'products': products})
