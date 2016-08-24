from django.conf.urls import url,include
from . import views

#
urlpatterns=[
url(r'^sign_up/', views.Sign_up_v,name='Sign_up'),]
