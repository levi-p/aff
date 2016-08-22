from django.shortcuts import render
from .models import Home_page_pics,Social_ps,place_details

from forms import search_form
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.

def details(request):
    P_details=place_details.objects.all()
    return render(request,'details.html',locals())

@login_required
def All_details(request,place_id):
    P2_details=place_details.objects.get(pk=place_id)
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
                results = place_details.objects.filter(g)
                if list(results)==[]:
                    result2='No results found'
                
            except: result2='No results found'
   


    return render(request,'search_results.html',locals())
