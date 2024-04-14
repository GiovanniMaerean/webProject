# README

The web application "steam app" is an application that will allow the user to use the Steam API to obtain information about how users interact with Steam and its products, developers, publishers...

## DEPENDENCIES
To run all the dependencies of the web application, they can be installed using the poetry command:

```poetry
poetry install
```


## EXECUTION STEPS
### Step 1

Navigate to the application directory, open the terminal, and generate migrations using the command:

```python
python manage.py makemigrations
```

### Step 2
Apply the generated migrations using the command:

```python
python manage.py migrate
```

### Step 3
Run the web application using the command:

```python
python manage.py runserver
```

### Step 4
Open a browser and enter the server IP of the web application. By default, this IP address is "http://127.0.0.1:8000/".


## CREATE SUPERUSER
Once we have created and applied the migrations, we can create a superuser, which will allow us to access the admin view, from where we can create and delete model instances with complete freedom, as well as edit them.

To create a superuser, we should use the command:

```python
python manage.py createsuperuser
```

Now we should run the application server and add "/admin" to the base URL, which in the case of the default IP would be "http://127.0.0.1:8000/admin/".

## USING THE APPLICATION
### LOGIN OR REGISTRATION
Upon entering the application server, we will be prompted to log in or register. If the user does not already have an account, they must register and then log in. If the user already has an account, they can log in directly.

### MAIN PAGE
Once we have logged in, we will be taken to the main page, where we will currently see a greeting to the user who has logged in and also have a "Log Out" button to log out.

## EXECUTION STEPS WITH DOCKER

Instead of running the server locally, it can be run using docker.

### Step 1



Navigate to the application directory, open the terminal, and bauild an image using the command:


```python
docker build -t name .
```

Now, instead of using "python manage.py runserver" to run the server locally, the next step to run the server will be, go to Docker desktop, run the built image, click on optionale settings, give the container a custom name (optional),  select a port (enter “0” to assign randomly generated host ports), run the image and finally the server will be running on the assigned port that can be found in "Containers" -> "Port(s)"



Repository link: https://github.com/GiovanniMaerean/webProject
