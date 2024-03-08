from django.http import HttpResponse
def main(request):
  return HttpResponse("<b>Welcome!!!</b>")
def aboutus(request):
  return HttpResponse("<b>ABOUT-US</b>")