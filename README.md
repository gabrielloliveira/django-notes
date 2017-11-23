# Django-Notes
Simple application of notes created with Django Framework

by: [gabrielloliveira](https://gabrielloliveira.com)

## Requirements
- Python - 3.6

## Installation
- Clone the repository
- Enter in the project folder ``` cd django-notes/ ```
- Create a virtualenv with ``` python3.6 -m venv env ```
- Activate the virtualenv ``` source /env/bin/activate ```
- Install the requirements ``` pip install -r requirements.txt ```
- Enter in the folder **notes** ``` cd notes/ ``` 
- Execute the migrations of the app ``` python manage.py migrate ```
- Create a **superuser** ``` python manage.py createsuperuser ```
- Run the application ``` python manage.py runserver ```
- Open your browser on [localhost:8000](http://localhost:8000)