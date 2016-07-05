from django.shortcuts import render
from details.models import Home_page_pic,Place_details
from forms import search_form
from django.db.models import Q

def home(request):
    H_p=Home_page_pic.objects.get(_active='eya')
    
    if request.method=='GET':
        form=search_form(request.POST)
        qr=request.GET.get('q','')
        if qr!='':
            
            try:
                g=(Q(Location__icontains=qr)|
                   Q(Name__icontains=qr)|
                   Q(Discription__icontains=qr))
                results = Place_details.objects.filter(g)
                if list(results)==[]:
                    result2='No results found'
                
            except: result2='No results found'
   
    
    
    return render(request,'base.html',locals())

def About(request):
    return render(request,'about.html',locals())
