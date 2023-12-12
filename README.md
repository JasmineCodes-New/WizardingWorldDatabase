# WizardingWorldDatabase

INF 601 - Advanced Programming with Python

Jasmine Irvin

Final Project

## Description
This project will be using Django to create a simple application for this project module. 
It makes use of Python, Django, and Bootstrap CSS. 

## Pip Install Instructions
It is essential you run this command so all the required installs are imported to your computer.
```
pip install -r requirements.txt
```

## Database
For the database you need to run: 
```
python manage.py makemigrations
```
Then:
```
python manage.py migrate
```
Finally:
```
python manage.py createsuperuser
```

This will create any SQL entries that need to go into the database, apply the migrations, and finally create an 
administrator login for the admin side of the project

## Running Project
To run the project, you will need to run the command in the terminal:
```
python manage.py runserver
```
or you can hit the run button in the pycharm IDE. It will take you to localhost:8000 and you will add
/admin to go the admin page or /polls to go to the polls page
