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


def detailedSearch(request, app_id):
    response = requests.get(f'https://store.steampowered.com/api/appdetails?appids={app_id}')
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()

        app_data = {}

        if str(app_id) in data:
            print("Goooood")
            app_info = data[str(app_id)]['data']
            # Lista de atributos que deseas incluir en el contexto
            attributes_to_include = ['type','name','steam_appid','required_age','is_free', 'short_description','supported_languages', 'release_date', 'platforms',
                                     'developers', 'publishers']

            for attribute in attributes_to_include:
                if attribute in app_info:
                    app_data[attribute] = app_info[attribute]
                else:
                    app_data[attribute] = None

            if 'price_overview' in app_info:
                price_overview = app_info['price_overview']
                app_data['discount_percent'] = price_overview.get('discount_percent')
                app_data['final_formatted'] = price_overview.get('final_formatted')

            if 'metacritic' in app_info:
                metacritic = app_info['metacritic']
                app_data['metacritic'] = metacritic.get('score')


    else:
        app_data = None

    print(app_data)

    return render(request, 'detailed_search.html', {'app_data': app_data})

def modifyProduct(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    else:
        form = ProductForm(instance=product)
    context = {'product': product, 'form': form}
    return render(request, 'modifyProduct.html', context)

