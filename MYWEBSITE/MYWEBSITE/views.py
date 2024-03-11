from django.http import HttpResponse
from django.shortcuts import render
def main(request):
  return HttpResponse("<b>Welcome!!!</b>")
def aboutus(request):
  return HttpResponse("<b>ABOUT-US</b>")
def course(request,courseid):
  return HttpResponse(courseid)
def homepage(request):
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
  return render(request,"index.html",data)
def product(request):
  return render(request,"products.html")