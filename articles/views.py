from django.shortcuts import render
from .models import Comments,Article_details

# Create your views here.

def art_list(request):
    P_list=Article_details.objects.all()
    return render(request,'post_list.html',locals())

def Article_view(request,article_id):
    artic = Article_details.objects.get(pk=article_id)
    return render(request,'articles.html',locals())
    
