from django.shortcuts import render
from details.models import Home_page_pic

def home(request):
    H_p=Home_page_pic.objects.get(_active='eya')
    
    
    return render(request,'base.html',locals())

def About(request):
    return render(request,'about.html',locals())
