from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import userforms
from service.models import Service
from news.models import News
from contactenquiry.models import contactEnquiry
from django.core.mail import send_mail
def  modeldata(request):
  servicesData=Service.objects.all()
  for a in servicesData:
    print(a)
  return render(request,"modeldata.html")
def main(request):
  return HttpResponse("<b>Welcome!!!</b>")
def pd(request):
  return render(request,"products.html")
from django.shortcuts import render
def evenodd(request):
  c=''
  if request.method=="POST":
    n=eval(request.POST.get('num1'))
    if n%2==0:
      c="EvenNumber"
    else:
      c="oddNumber"
  return render(request,"evenodd.html",{'c':c})
def calculator(request):
    c = ''
    if request.method == "POST":  # Check if the request method is POST
        try:
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2
        except Exception as e:  # Catch any exceptions
            c = "Invalid operation or input"
    return render(request, "calculator.html", {'c': c})  # Pass the calculated value to the template

def course(request,courseid):
  return HttpResponse(courseid)
def homepage(request):
  'Testing Mail',
  'Here is the message',
  'rk6961609@gmail.com',
  ['rajesh.2125it1020@kiet.edu'],
  fail_silently=False,
  newsData = News.objects.all();
  data = {
    # 'title':'Home Page',
    # 'bodytext':'Welcome To HomePage',
    # 'clist':['Django','Python','Java','HTML','CSS','JS'],
    # 'studentdetails':[
    #   {'phoneNo':'8859655963','Name':'Rajesh Kumar'},
    #   {'phoneNo':'8859655966','Name':'Raju'}
    # ],
    # 'numbers':[]
    'newsData':newsData
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
# def marksheet(request):
#   if request.method=="POST":
#     n1=request.POST.get('subject1')
#     n2=request.POST.get('subject2')
#     n3=request.POST.get('subject3')
#     n4=request.POST.get('subject4')
#     n5=request.POST.get('subject5')
#     c=n1+n2+n3+n4+n5
#     c1=(n1+n2+n3+n4+n5)//5  
#     return render(request,"Marksheet.html")
#   return render(request,"Marksheet.html")
from django.shortcuts import render

def marksheet(request):
    if request.method == "POST":
        # Retrieve the subject scores from the POST data and convert them to integers
        n1 = int(request.POST.get('subject1'))
        n2 = int(request.POST.get('subject2'))
        n3 = int(request.POST.get('subject3'))
        n4 = int(request.POST.get('subject4'))
        n5 = int(request.POST.get('subject5'))
        
        # Calculate the total score
        total_score = n1 + n2 + n3 + n4 + n5
        
        # Calculate the average score
        average_score = total_score // 5
        
        # Render the Marksheet.html template with the calculated values passed as context
        return render(request, "Marksheet.html", {'total_score': total_score, 'average_score': average_score})
    
    # If the request method is not POST, just render the Marksheet.html template
    return render(request, "Marksheet.html")
def newsdetails(request,id):
   return render(request, "newsdetails.html")
def ContactForm(request):
   return render(request,"ContactForm.html")
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