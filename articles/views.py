from django.shortcuts import render
from .models import Comments,Article_details
#from zinnia.markups import html_format

# Create your views here.

def art_list(request):
    P_list=Article_details.objects.all()
    return render(request,'post_list.html',locals())

def Article_view(request,article_id):
    artic = Article_details.objects.get(pk=article_id)
    #html_article= html_format(artic.Article)
    return render(request,'articles.html',locals())
    
