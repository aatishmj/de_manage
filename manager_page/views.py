from django.shortcuts import render , redirect
from django.contrib.auth import authenticate 
from django.contrib.auth import logout , login
import requests
from django.contrib.auth.decorators import login_required

@login_required
def dash(request):
    response=requests.get(url="https://aatish13.pythonanywhere.com/employee_work/")
    data=response.json()
    response=requests.get(url="https://aatish13.pythonanywhere.com/api/employees/")
    data1=response.json()
    name_list =[]

    for items in data1 :
        name=items["name"]
        name_list.append(name)

    context={
        "api_data": data,
        "names" :name_list
    }
    print(context)
    return render(request,"ad_page.html", context)

def admin_login(request) :
    
    if request.user.is_authenticated:
        return redirect("dash")
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

@login_required
def add_emp(request) :
    api_url = 'https://aatish13.pythonanywhere.com/api/employees/'
    if request.method =="POST" :
        name = request.POST["name"]        
        email = request.POST["email"]
        phone_no = request.POST["phone_no"] 
        data = {
            "name":name,
            "email":email,
            "phone_no":phone_no,
            }
        response=requests.post(api_url, data=data)

    return render(request,"sign.html")

def sign(request) :
    if request.method =="POST" :
        name = request.POST["name"]
        password = request.POST["password"]
    return render(request, "sign.html")



def upload(request):
    api_url = 'https://aatish13.pythonanywhere.com/api/admin/'
    
    if request.method == "POST":
        name = request.POST.get("name")  # Use the correct field name from your HTML form
        image = request.FILES.get("image")  # Use the correct field name from your HTML form
        
        data = {
            "name": name,
        }
        
        files = {
            "drawing": image,
        }
        
        response = requests.post(api_url, data=data, files=files)
        
        if response.status_code == 201:
            print('Name and image added successfully!')
        else:
            print("Error:", response.status_code)
    
    return render(request, "upload.html")
