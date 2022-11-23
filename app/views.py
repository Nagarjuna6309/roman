from django.shortcuts import render

# Create your views here.
def roman(request):
    d={'name':'BROCK LESNAR'}
    return render(request,"roman.html",d)