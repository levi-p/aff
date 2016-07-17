from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^details/',views.details,name='details'),
    url(r'^all_details/(?P<place_id>[0-9]+)',views.All_details,name='Place_details'),
    url(r'^search_results/',views.search_results,name='search_results')
]
