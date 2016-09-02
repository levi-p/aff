"""accom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^sign_up/', include('register.urls', namespace='Sign_up')),
    url(r'^booking/', include('booking.urls',namespace='book')),
    url(r'^booking/', include('register.urls',namespace='reg')),
    url('^', include('django.contrib.auth.urls')),
    #url(r'^accounts/login/$', auth_views.login ,name='login'),
    #url(r'^accounts/login/$', auth_views.password_reset),
    url(r'^accounts/profile/$', views.home),
    url(r'^about/', views.About, name='about'),
    url(r'^search/', views.search, name='search'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home ,name='home'),
    url(r'^d/',include('details.urls',namespace='Det'), name='details'),
    url(r'^c/',include('articles.urls',namespace='art')),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})]
