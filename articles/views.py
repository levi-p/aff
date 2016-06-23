from django.shortcuts import render
from .models import Comments,Article_details

# Create your views here.

def Article_view(request,i_d=1):
    arti = Article_details.objects.get(pk=i_d)
    return render(request,'articles.html',locals())
    
