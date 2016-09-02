from django.shortcuts import render,redirect
from .forms import Sign_up_form 
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Sign_up
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login


# Create your views here.

#@csrf_protect
def Sign_up_v(request):
    
        
        form=Sign_up_form(request.POST)
        if form.is_valid():
            Username=form.cleaned_data['Name']
            #Email=form.cleaned_data['Email']
            password1 = form.cleaned_data['password']
            password2=form.cleaned_data['enter_password']
            
            if password1 == password2 : 
                #form.save()
                #d=Sign_up(Username,Email,password1)
                #d.save()
                user=User.objects.create_user(Username,'youremail@email.com',password1)
                user.save()
                logde=authenticate(username=form.cleaned_data['Name'],password=form.cleaned_data['password'])

                login(request,logde)
                return redirect('/')
                
                
            else:
                pass
    #else:
     #   form=Sign_up_form()

        return render(request,'sign_up.html',locals())



