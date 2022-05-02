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

# =================== 3
add react
cd music_controller
install npm

we will create new app called frontend
- django-admin startapp frontend
cd frontend
create folders templates, static.., src 
npm init -y
npm i webpack webpack-cli --save-dev

npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
npm i react react-dom --save-dev
npm install @material-ui/core

npm ERR! Could not resolve dependency:
https://stackoverflow.com/questions/64573177/unable-to-resolve-dependency-tree-error-when-installing-npm-packages

npm install @material-ui/core --legacy-peer-deps
npm install @babel/plugin-proposal-class-properties
npm install react-router-dom
npm install @material-ui/icons --legacy-peer-deps

in frontend folder create babel.config.json

git ignore https://github.com/rtancman/react-material-ui-auth/blob/master/.gitignore

in frontend folder webpack.config.js
 bunldle our js scripts to one file
package.json

in floder src make file index.js
in folder /templates/frontend/index.html

/frontend/views.py
create /frontend/urls.py

/music_controller/urls.py
add route

create react component
create /frontend/src/components/App.js
- here we create react component which will return the stuff rendered to div
/frontend/src/index.js
- here we pack ur javascript stuff by webpack

npm run dev
inside folder /frontend/static/frontend/main.js
there is gibberish representing packed javascript by webpack

/music_controller/settings.py
we have to add our app
