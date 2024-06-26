"""
URL configuration for MYWEBSITE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MYWEBSITE import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('main-page/',views.main),
    path('pd/',views.pd,name="product"),
    path('course-details/<int:courseid>',views.course),
    path('',views.homepage),
    path('products-page/',views.product),
    path('th/',views.thank),
    path('submitform',views.submitform,name="submitform"),
    path('userform',views.userform),
    path('calculator',views.calculator),
    path('evenodd',views.evenodd),
    path('marksheet',views.marksheet),
    path("modeldata",views.modeldata),
    path('newsDetails/<id>',views.newsdetails),
    path('contactform',views.ContactForm),
    path('saveEnquiry',views.saveEnquiry,name="saveEnquiry"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
