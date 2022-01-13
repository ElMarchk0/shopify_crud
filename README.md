# CRUD app for Shopify internship application

This app is designed to perform CRUD operations as well as sort and filter databases. It was built using Python and Django. The GUI is generated by the Django rest framework library.

This app is designed to allow a user to input and sort products within a database. There are search, ordering and filtering options created by the app that generate urls that can be used in headers for GET, POST, PATCH and DELETE requests, as well as filtering, search, and sort functions. 

To start the app:

On Mac/Linux:
> python3 -m pip install --upgrade pip

> pip3 install virtualenv

> git clone https://github.com/ElMarchk0/shopify_crud.git

> cd shopify_crud

> python3 -m venv env

> source env/bin/activate

> pip install -r requirements.txt

> python manage.py runserver

On Windows:
> python3 -m pip install --upgrade pip

> pip3 install virtualenv

> git clone https://github.com/ElMarchk0/shopify_crud.git

> cd shopify_crud

> python3 -m venv env

> source env/scripts/activate

> pip install -r requirements.txt

> python manage.py runserver

Goto http://localhost:8000/api

To view an individual product go to https://localhost:8000/api/ {paste id here}