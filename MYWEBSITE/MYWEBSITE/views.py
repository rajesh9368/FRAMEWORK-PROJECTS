from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import userforms
def main(request):
  return HttpResponse("<b>Welcome!!!</b>")
def pd(request):
  return render(request,"products.html")
def calculator(request):
  c=''
  try:
    if request.mrthpod=="POST":
      n1=eval(request.POST.get('num1'))
      n2=eval(request.POST.get('num2'))
      opr=request.POST.get('opr')
      if opr=="+":
        c=n1+n2
      elif opr=="-":
        c=n1-n2
      elif opr=="*":
        c=n1*n2
      elif opr=="/":
        c=n1/n2
      print(c)
  except:
    c="Invalid opr..."
  return render(request,"calculator.html")
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
def thank(request):
  return render(request,"Thankyou.html")
# def submitform(request):
#   return HttpResponse(request)
def submitform(request):
  fn = userforms()
  data = {'form':fn}
  finalans=0
  # data={}
  try:
    if request.method=="POST":
      n1=int(request.POST.get('num-1'))
      n2 = int(request.POST.get('num-2'))
      finalans=n1+n2
      data={
        # 'n1':n1,
        # 'n2':n2,
        'form':fn,
        'finalans':finalans
      }
      url = "/th/?output={}".format(finalans)
      # return HttpResponseRedirect(url)
      return HttpResponse(finalans)
  except:
    pass 
  return render(request,"userForm.html",data)

def userform(request):
  finalans=0
  data={}
  try:
    if request.method=="POST":
      n1=int(request.POST.get('num-1'))
      n2 = int(request.POST.get('num-2'))
      finalans=n1+n2
      data={
        'n1':n1,
        'n2':n2,
        'finalans':finalans
      }
      url = "/th/?output={}".format(finalans)
      return HttpResponseRedirect(url)
      # return HttpResponseRedirect('/th/')
  except:
    pass 
  return render(request,"userForm.html",data)
