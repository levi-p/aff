from django.shortcuts import render
from .models import Place_details

# Create your views here.

def details(request):
    P_details=Place_details.objects.all()
    return render(request,'details.html',locals())

def All_details(request,place_id):
    P2_details=Place_details.objects.get(pk=place_id)
    return render(request,'place_details.html',locals())
