from django.shortcuts import render
from .models import Place_details

# Create your views here.

def details(request):
    P_details=Place_details.objects.all()
    return render(request,'details.html',locals())
    
