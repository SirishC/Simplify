# Simplify | Web Application

URL shortener using Django and Delpoying on Heroku.
# getting started

### Setting Up Virtual Environment for Django in Linux/Mac.
To set up we need to install certain libraries . 
>  **virtualenv** installation.
```sh
    $ pip install virtualenv 
```
> creating a virtual environment folder.
```sh
    $ virtualenv python_virtual_env
    $ cd python_virtual_env
```
> activate the virtual environment.
```sh
    $ source bin/activate 
    (python_virtual_env)$
```
 >we are done setting up virtual environment ! <br>
 >Now let us install Django in the virtual environment <br>
 > **Django** installation is very simple <br>
``` sh 
    (python_virtual_env)$pip install django 
```
> we need to create a project to work on. 
``` sh 
    (python_virtual_env)$ django-admin.py startproject Simple
    (python_virtual_env)$ cd Simple 
```
> we have to create a superuser who is similar to an admin.
``` sh 
    (python_virtual_env)$ python manage.py createsuperuser 
``` 
> It will prompts certain requirements like username , email , passwords .. <br>
**We have finish setting up our first Djando server.**
```sh
    (python_virtual_env)$ python manage.py runserver
```

great🤟 :)<br>
progress █████▒▒▒▒▒ 50 %

___

# Creating an App for our project.
>Now to create an app we have to run 
```sh
    (python_virtual_env)$ python manage.py startapp simplify 
```
> it can be any name.
### We Are All set to build a web application. Cool:)! 

___
# Web Applications
> Automatically should create a shortcode of each url <br>
> push it into the sqlite3(initially) <br>
> When the link already in the database same shortcode will be given. <br>

progress ████████▒▒ 80 % <br>
Awesome ! <br>

# Deploy live on Heroku
> Requirements 

```sh
(python_virtual_env)$pip install heroku 
(python_virtual_env)$pip install django-heroku
(python_virtual_env)$pip install psycopg2
(python_virtual_env)$pip install whitenoise
(python_virtual_env)$pip install gunicorn
```
> Create a Procfile and a requirements.txt  and configuration <br>
*[How to do it ](https://devcenter.heroku.com/articles/deploying-python)* <br>
> Djando app while deploying on heroku there may be errors due to static files <br>
> Configuration of static files <br>
*[Static files](https://docs.djangoproject.com/en/2.2/howto/static-files/)* <br>
> Since heroku provides postgresql so we have to configure postgresql<br>
*[Full Configuration](https://devcenter.heroku.com/articles/django-app-configuration)* <br>
> Finally on , Heroku Server where our app is running we have to run <br>
```sh
    $python manage.py migrate
```
> #### OUR APP IS UP IN RUNNING !! AWESOME !! <br>
#### ██████████ 100% Successfully Done ! <br>
# References
> [CodeForEntrepreneurs](https://www.codingforentrepreneurs.com) they are awesome
____
