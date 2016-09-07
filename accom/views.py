from django.shortcuts import render
from details.models import Home_page_pics,place_details,Social_ps
from forms import search_form
from django.db.models import Q
from django.http import HttpResponseRedirect

def home(request):
    H_p=Home_page_pics.objects.filter(_active='eya')
    sp=Social_ps.objects.filter(_active='owo')
    
            #return HttpResponseRedirect('results.html')
            
   
    
    
    return render(request,'base.html',locals())

def search(request):
    if request.method=='GET':
        form=search_form(request.POST)
        qr=request.GET.get('q','')
        if qr!='':
            
            try:
                g=(Q(Location__icontains=qr)|
                   Q(Name__icontains=qr))
                   #Q(Discription__icontains=qr))
                results = place_details.objects.filter(g)
                if list(results)==[]:
                    result2='No results found'
                
            except: result2='No results found'
    
    return render(request,'search_results.html',locals())






def About(request):
    return render(request,'about.html',locals())
