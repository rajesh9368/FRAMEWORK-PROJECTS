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

# Order a query in ascendind or descending => 
=> Ascending -> ('service-title')
=>Descending -> ('-service-title') i.e -is placed to put all in descending order .

# Limiting query in Django =>
=> is slicing operator Example=> .[2:5],[3] but it never supports negative index .

# Custom Template filters in Django => 
 => autoescape
block
comment
csrf_token
cycle
debug
extends
filter
firstof
for
for … empty
if
Boolean operators
== operator
!= operator
< operator
> operator
<= operator
>= operator
in operator
not in operator
is operator
is not operator
Filters
Complex expressions
ifchanged
include
load
lorem
now
regroup
Grouping on other properties
resetcycle
spaceless
templatetag
url
verbatim
widthratio
with
Built-in filter reference
add
addslashes
capfirst
center
cut
date
default
default_if_none
dictsort
dictsortreversed
divisibleby
escape
escapejs
escapeseq
filesizeformat
first
floatformat
force_escape
get_digit
iriencode
join
json_script
last
length
length_is
linebreaks
linebreaksbr
linenumbers
ljust
lower
make_list
phone2numeric
pluralize
pprint
random
rjust
safe
safeseq
slice
slugify
stringformat
striptags
time
timesince
timeuntil
title
truncatechars
truncatechars_html
truncatewords
truncatewords_html
unordered_list
upper
urlencode
urlize
urlizetrunc
wordcount
wordwrap
yesno
Internationalization tags and filters
i18n
l10n
tz
Other tags and filters libraries
django.contrib.humanize
static
static
get_static_prefix
get_media_prefix


# Django TinyMCE Editor Integration with NewsApp :-
  => pip install django-tinymce
  => Now create newsapp = > python manage.py startapp  Newsapp 
  inside models.py file => 
  ex :- from django.db import models
from tinymce.models import HTMLField
class News(models.Model):
  news_title = models.CharField(max_length=100)
  news_desc = HTMLField()

  => inside admin.py file:-
        from django.contrib import admin
from news.models import News
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
  list_display = ('news_title','news_desc')
admin.site.register(News,NewsAdmin)

=> python manage.py makemigrations
=> python manage.py migrate
=> Now check for all created models in 0001_initial.py file.

# Display News in Marquee Tag(Dynamic) :-

=>inside views.py file Example :-
           from news.models import News
def homepage(request):
  newsData = News.objects.all();
  data = {
    
    'newsData':newsData
  }
  return render(request,"index.html",data)

=> inside index.html file :-
                    <marquee><a href = "">{%for news in newsData%}
                    {{news.news_title}}</a> &nbsp; &nbsp; &nbsp;
                    {%endfor%}
                    </marquee>

# Reset Django admin password :-
   => A user must known about user_id
   =>  python manage.py changepassword username

# Saving Form data to the databse:-
    =>create form with some input fields
    => create new app an d update its model.py and admin.py and also migrate its tables
    inside views.py for example code :-
        def saveEnquiry(request):
  # n=''
  if(request.method=="POST"):
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    website=request.POST.get('website')
    message=request.POST.get('message')
    en=contactEnquiry(name=name,email=email,phone=phone,website=website,message=message)
    en.save()
    # n='Data Inserted'
  return render(request,"ContactForm.html");


<form action="{% url 'saveEnquiry' %}" method="POST">
  {%csrf_token%}
  Name <input type="text" name="name">
  Email <input type="Email" name="email">
  Phone <input type="number" name="phone">
  website Name<input type="text" name="websitename">
  Message<input type="textarea" name="message">
  <button>submit</button>


from django.db import models
# Create your models here.
class contactEnquiry(models.Model):
  name=models.CharField(max_length=50)
  email=models.CharField(max_length=60)
  phone=models.CharField(max_length=50)
  website=models.CharField(max_length=70)
  message=models.TextField()


from django.contrib import admin
from contactenquiry.models import contactEnquiry
# Register your models here.
class CN(admin.ModelAdmin):
  list_display = ('name','email','phone','website','message')
admin.site.register(contactEnquiry,CN)
# Register your models here.


# FileUpload in djangoModel in AdminPanel FileField() :-
=> in settings.py file of an app
  MEDIA_ROOT = BASE_DIR/"media"
  MEDIA_URL="/media/"

=> in urls.py file of an app :-
from django.conf import settings
from django.conf.urls.static import static

  if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 => in models.py file of an app
 news_image=models.FileField(upload_to="news/",max_length=250,null=True,default=None)

# Display uploaded image in the template :-
<img src = "/media/{{newsDetails.news-image}}"/>

# Sending Email & SMTP setup in Django :-
    => inside settings.py file :-
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='rk6961609@gmail.com'
EMAIL_HOST_PASSWORD=''
EMAIL_USE_TLS=True

         =>inside views.py file :-
           from django.core.mail import send_mail

  'Testing Mail',
  'Here is the message',
  'rk6961609@gmail.com',
  ['rajesh.2125it1020@kiet.edu'],
  fail_silently=False,

# Email MultiAlternatives:-
       from django.core.mail import send_mail,EmailAlternatives
      Ex:-  EailMultiAlternatives(subject,msg,from_email,[to])
        msg.content_subtype = 'html
        msg.send()







  







