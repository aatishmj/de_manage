from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout , login


def dash(request):
    if request.method=="POST" :
      pass
    return render(request,"admin_upload.html")

def admin_login(request) :
    if request.method =="POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dash")
        else:
            return render(request ,"loginpage.html") 
        
    return render(request ,"loginpage.html")

def add_emp(request) :
    return render(request,"indi.html")
   