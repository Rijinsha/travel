from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pswrd = request.POST['password']
        user = auth.authenticate(username=uname, password=pswrd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credential")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    #fech data
    if request.method== 'POST':
        username= request.POST['usrname']
        fname = request.POST['firstname']#here firstname is the name of register.html
        lname=request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword= request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')  #refresh register page
            elif User.objects.filter(email=email).exists():   #else check email allso
                messages.info(request,"email Taken")
                return redirect('register')
            else:
               user =User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname,email=email)
               user.save();
            print("user created")
        else:
            messages.info(request,"password not matched")
            #print("password not maching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')