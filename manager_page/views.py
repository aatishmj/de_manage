from django.shortcuts import render , HttpResponse

# Create your views here.
def dash(request):
    return HttpResponse("dash")