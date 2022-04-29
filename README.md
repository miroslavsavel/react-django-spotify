# react-django-spotify

https://www.youtube.com/watch?v=JD-age0BPVo&list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j

VS code extension 
- prettier
- python
- django
- ES7 react
- javascript ES6

Instalation
- pip install django djangorestframework

- django-admin startproject music_controller
this is the name of our app

- error - on win fixed this way:
django-admin : The term 'django-admin' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path   
was included, verify that the path is correct and try again.
https://stackoverflow.com/questions/23439089/using-django-admin-on-windows-powershell/23439909#23439909
pip uninstall django
python -m pip install --upgrade pip
pip install django djangorestframework
pip install django-binary-database-files        !!!!!!!!! fix start django admin on powershell

WARNING: The script django-admin.exe is installed in 'C:\Users\Šavel\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

- django-admin startproject music_controller
it will create a project folder
- cd music_controller
- django-admin startapp api
install app inside project folder

add app to project
- settings.py - installed_apps
add also rest_framework

# creating first view
- api/views.py
create function returning string here

create file api/urls.py

in music_controllers/urls.py
add route to the api.urls

api/urls.py

# making migrations
python .\manage.py makemigrations
we have to update database to store current changes to the app
python .\manage.py migrate
file db.sqlite3 showed up

# run server
python .\manage.py runserver


# 2 creating model
-/api/models.py
here we create new table (model in this case) with unique code
-in music_controller folder
python .\manage.py makemigrations
make migrations
python .\manage.py migrate
apply migration

# creating api endpoint
/api/serializers.py
Serialier class
/api/views.py

/api/urls.py