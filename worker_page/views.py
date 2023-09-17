from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout , login

def emp_login(request) :
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
   
def emp_dash(request) :
    return render(request , "emp_dash.html")
