# FRAMEWORK-PROJECTS
**DJANGO,PYTHON**
# LINK :- https://www.djangoproject.com/
# Framework :-
=> A framework is a particular set of rules , ideas or beliefs which you use in order to deal with problems or to decide what to do.
=> While Library involves custom based(pre defined).
=> Django is basically a high level python application framework that enables rapid development of web applications.
=> Open source Python Framework.
=> Follows the model view Template(MVT) Architecture.
=> Most popular python framework.
# Why Django :-
=> It is fast and simple
=> It is secure
=> It suits any web application projects
=> Well Established
=> MVT support and object orientation
=> Built in Authentication and Authorization
=> Packaging System
# Companies Using Django :-
=> Example : youtube,spotify,pinterest,Mozilla,Atlassian,Udemy etc.
# Pre requisites For Django :-
=> Basics of Pyhton
=> HTML,CSS,JSFndamentals
# MVT(Model View Template) :-
=> MVT is Software design patytern.
# MODEL :-
Model going to acts as a inteface of your data(i.e your database,schema,model,table)
# View :-
View is the user interface you see in your browser when render a website ( through functions and classes)
# Template :-
A template consists of static parts of the desired HTML output as some specila syntax describing how dynamic content will be inserted.
# Flow Diagram
User <==> Django <==> URL <==> view <==> Model/Template
# Comprises of files mainly :-
  # Manage.py :- 
  To run the server
  # Settings.py :-
  It is the main file which comprises all the setting files related to the website
  Intalled app,Middleware,Templates,SQLite(Default Database),static,authentication validator etc.
  # urls.py : - 
  To take all the urls of the view 
  # views.py :-
  Is created to render all the user interfaces and connected to their urls. 
# Urls and Views :-
 => Urls are also called as **routes**
 # views :-
 => The logic is executed for differnet URLs(http method) 
# Creating Urls and views in Django
 => Inside views.py  
 # from django.http import HttpResponse (this HttpResponse for text based requesting Output)
 # Example :- 
def main(request):
  return HttpResponse("<b>Welcome!!!</b>")
def aboutus(request):
  return HttpResponse("<b>ABOUT-US</b>")

  => Now inside urls.py import all views 
  # from MYWEBSITE import views
  # Example :-  path('main-page/',views.main),path('about-us/',views.aboutus),
# Creating dynamic urls in Django:-
=> Routing can be done in three types :-
    => int,str,slug  Example :- <int:name>
# Passing data from django View to template 
Example :-
        =>    def homepage(request):
  data = {
    'title':'Home Page',
    'bodytext':'Welcome To HomePage',
    'clist':['Django','Python','Java','HTML','CSS','JS'],
    'studentdetails':[
      {'phoneNo':'8859655963','Name':'Rajesh Kumar'},
      {'phoneNo':'8859655966','Name':'Raju'}
    ],
    'numbers':[]
  }
# Django template using looping statement if elif else statement:
# Managing static Files: - 
# HTML Header and Footer in Django HTML Template include :
# How to highlight active links in django:
# what are HTTP Request methods in django: Differ between get and post
# Implementation of get an post method(CSRF token)
# Page redirections in django
# Django html form action url
# form tutorial for beginners
# Commands 
=> Install Python
=>python --version
=>pip install django
=>pip freeze
=>django-admin
   =>check
   => compilemessages
    =>createcachetable
    =>dbshell
    =>diffsettings
    =>dumpdata
    =>flush
    =>inspectdb
    =>loaddata
    =>makemessages
    =>makemigrations
    =>migrate
    =>optimizemigration
    =>runserver
    =>sendtestemail
    =>shell
    =>showmigrations
    =>sqlflush
    =>sqlmigrate
    =>sqlsequencereset
    =>squashmigrations
    =>startapp
    =>startproject
    =>test
    =>testserver
  # from django.http import HttpResponse (this HttpResponse for text based requesting Output)
# Create a new Project :- django-admin startproject projectname
# Starting a development server :- python manage.py runserver portno
# MAKING DEFAULT MIGRATIONS :- python manage.py makemigrations(whiile create a new model) ,   pyhton manage.py migrate(while performing CRUD operations in already created model)
# Create Superuser in Django :- python manage.py createsuperuser
# from MYWEBSITE import views (To import The views) 
# from django.http import HttpResponse (this HttpResponse for text based requesting Output).
# for render an html file => from django.shortcuts import render 
# Managing static Files  => 
STATICFILES_DIRS = [
    BASE_DIR,"static"
]          or yo can also do using {% load static %}  example '{% static "address of image" % }'
# HTML Header and Footer in Django HTML Template include :-
{% include  "header.html" %} //body  {% include "footer.html %}

# extends Django Template Tags =>
 {% include  "header.html" %} 
 {% block bloackname %}
 {% endblock %}
 {% include "footer.html %}
 Now extends this in the required area 

 # Django URL Template Tags => 
 {% url 'name' %}
**Example**
path('pd/',views.pd,name="product")
<li><a href="{% url 'product' %}">Products</a></li>




