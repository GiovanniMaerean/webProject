import requests
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from steamApp.forms import ProductForm, DeveloperForm, PublisherForm, SteamUserForm
from steamApp.models import Product, Publisher, Developer, SteamUser


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


def search(request, inputValue):
    search_value = inputValue.lower()
    products = []
    page = request.GET.get('page', 1)
    response = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')

    if response.status_code == 200:
        app_list = response.json()['applist']['apps']
        products = [{'appid': app['appid'], 'name': app['name']} for app in app_list if
                    app['name'].lower().startswith(search_value)]

        products.sort(key=lambda x: x['name'].lower())


    try:
        paginator = Paginator(products, 10)
        products = paginator.page(page)
    except:
        raise Http404

    context = {
        'search_value': search_value,
        'entity': products,
        'paginator': paginator
    }

    return render(request, 'search.html', context)



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

def createDeveloper(request):
    if request.method == 'POST':
        form = DeveloperForm(request.POST, user=request.user)
        if form.is_valid():
            developer = form.save(commit=False)
            developer.creatorUser = request.user
            selected_products = form.cleaned_data['products']
            numProducts = len(selected_products)
            developer.developedProducts = numProducts
            developer.save()
            developer.products.set(selected_products)
            return redirect('showDevelopers')
    else:
        form = DeveloperForm(user=request.user)
    context = {'form': form}
    return render(request, 'createDeveloper.html', context)

def showDevelopers(request):
    developers = Developer.objects.filter(creatorUser=request.user)
    context = {'developers': developers}
    return render(request, 'showDevelopers.html', context)

def createPublisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST, user=request.user)
        if form.is_valid():
            publisher = form.save(commit=False)
            publisher.creatorUser = request.user
            selected_products = form.cleaned_data['products']
            numProducts = len(selected_products)
            publisher.publishedProducts = numProducts
            publisher.save()
            publisher.products.set(selected_products)
            return redirect('showPublishers')

    else:
        form = PublisherForm(user=request.user)
    context = {'form': form}
    return render(request, 'createPublisher.html', context)

def showPublishers(request):
    publishers = Publisher.objects.filter(creatorUser=request.user)
    context = {'publishers': publishers}
    return render(request, 'showPublishers.html', context)

""" def showPublishers(request):
    publishers = Publisher.objects.all()  # Obtener el editor específico
    #products = publisher.publishedProducts  # Obtener todos los productos asociados al editor
    context = {'publishers': publishers}
    return render(request, 'showPublishers.html', context)"""


def createSteamUser(request):
    if request.method == 'POST':
        form = SteamUserForm(request.POST, user=request.user)
        if form.is_valid():
            steamUser = form.save(commit=False)
            steamUser.creatorUser = request.user
            friends = form.cleaned_data['friends']
            products = form.cleaned_data['products']
            steamUser.save()
            steamUser.friends.set(friends)
            steamUser.products.set(products)
            return redirect('showSteamUsers')

    else:
        form = SteamUserForm(user=request.user)
    context = {'form': form}
    return render(request, 'createSteamUser.html', context)

def showSteamUsers(request):
    steamUsers = SteamUser.objects.filter(creatorUser=request.user)
    context = {'steamUsers': steamUsers}
    return render(request, 'showSteamUsers.html', context)

def deletePublisher(request, id):
    publisher = get_object_or_404(Publisher, pk=id)
    publisher.delete()
    return redirect('showPublishers')

def deleteDeveloper(request, id):
    developer = get_object_or_404(Developer, pk=id)
    developer.delete()
    return redirect('showDevelopers')

def deleteSteamUser(request, id):
    steamUser = get_object_or_404(SteamUser, pk=id)
    steamUser.delete()
    return redirect('showSteamUsers')

def modifyDeveloper(request, id):
    developerObtained = Developer.objects.get(id=id)
    if request.method == 'POST':
        form = DeveloperForm(request.POST, user=request.user, instance=developerObtained)
        if form.is_valid():
            developer = form.save(commit=False)
            selected_products = form.cleaned_data['products']
            numProducts = len(selected_products)
            developer.developedProducts = numProducts
            developer.save()
            developer.products.set(selected_products)
            return redirect('showDevelopers')
    else:
        form = DeveloperForm(user=request.user, instance=developerObtained, initial={'name': developerObtained.name, 'products': developerObtained.products.all()})
    context = {'form': form, 'developer': developerObtained}
    return render(request, 'modifyDeveloper.html', context)

def modifyPublisher(request, id):
    publisherObtained = Publisher.objects.get(id=id)
    if request.method == 'POST':
        form = PublisherForm(request.POST, user=request.user, instance=publisherObtained)
        if form.is_valid():
            publisher = form.save(commit=False)
            publisher.creatorUser = request.user
            selected_products = form.cleaned_data['products']
            numProducts = len(selected_products)
            publisher.publishedProducts = numProducts
            publisher.save()
            publisher.products.set(selected_products)
            return redirect('showPublishers')

    else:
        form = PublisherForm(user=request.user, instance=publisherObtained, initial={'name': publisherObtained.name, 'products': publisherObtained.products.all()})
    context = {'form': form}
    return render(request, 'modifyPublisher.html', context)


def modifySteamUser(request, id):
    steamUserObtained = SteamUser.objects.get(id=id)
    if request.method == 'POST':
        form = SteamUserForm(request.POST, user=request.user, instance=steamUserObtained)
        if form.is_valid():
            steamUser = form.save(commit=False)
            steamUser.creatorUser = request.user
            friends = form.cleaned_data['friends']
            products = form.cleaned_data['products']
            steamUser.save()
            steamUser.friends.set(friends)
            steamUser.products.set(products)
            return redirect('showSteamUsers')

    else:
        form = SteamUserForm(user=request.user, instance=steamUserObtained, initial={'name': steamUserObtained.realName,
                                                                                     'friends': steamUserObtained.friends.all(),
                                                                                     'products': steamUserObtained.products.all()})
    context = {'form': form}
    return render(request, 'modifySteamUser.html', context)