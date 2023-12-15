from django.http import HttpResponse
from django.shortcuts import render
from .models import place, guide


# Create your views here.
#def home(request):
 #   return HttpResponse("THIS IS HOME PAGE")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def detail(request):
    return render(request,"details.html")
def thanks(request):
    return render(request,"thnks.html")
def calculation(request):
    return render(request,"amoprtn2.html")
def result(request):
    x=int(request.GET['num1'])
    y = int(request.GET['num2'])
    res1=x+y
    res2=x*y
    res3=x-y
    res4=x/y
    return render(request,"result2.html",{'add':res1,'mul':res2,'sub':res3,'div':res4})


#staticwebsite
def demo(request):
    #fech all datas kn the table in vabl name "obj"
    obj=place.objects.all()
    obj1 =guide.objects.all()
    return render(request,"index.html",{'result':obj,'guid':obj1})
