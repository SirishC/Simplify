# Simplify | Web Application

URL shortener using Django and Delpoying on Heroku 
# getting started

### Setting Up Virtual Environment for Django in Linux/Mac 
To set up we need to install certain libraries . 
>  **virtualenv** installation
```sh
    $ pip install virtualenv 
```
> creating a virtual environment folder 
```sh
    $ virtualenv python_virtual_env
    $ cd python_virtual_env
```
> activate the virtual environment 
```sh
    $ source bin/activate 
    (python_virtual_env)$
```
 >we are done setting up virtual environment !
 >Now let us install Django in the virtual environment
 > **Django** installation is very simple 
``` sh 
    (python_virtual_env)$pip install django 
```
> we need to create a project to work on ! 
``` sh 
    (python_virtual_env)$ django-admin.py startproject Simple
    (python_virtual_env)$ cd Simple 
```
> we have to create a superuser who is similar to admin !
``` sh 
    (python_virtual_env)$ python manage.py createsuperuser 
``` 
> will prompts certain requirements like username , email , passwords ..
**We have finished setting up our first Djando server.**
```sh
    (python_virtual_env)$ python manage.py runserver
```

great🤟 :)<br>
progress █▒▒▒▒▒▒▒▒▒ 10 % 

___

# Creating an App for our project.

