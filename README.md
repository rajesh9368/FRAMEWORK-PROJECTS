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
# CReating Urls and views in Django
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
# from django.http import HttpResponse (this HttpResponse for text based requesting Output)











