from django.shortcuts import render
from .models import Home_page_pics,Place_details,Social_ps

from forms import search_form
from django.db.models import Q


# Create your views here.

def details(request):
    P_details=Place_details.objects.all()
    return render(request,'details.html',locals())

def All_details(request,place_id):
    P2_details=Place_details.objects.get(pk=place_id)
    return render(request,'place_details.html',locals())


def search_results(request):

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
   


    return render(request,'search_results.html',locals())
