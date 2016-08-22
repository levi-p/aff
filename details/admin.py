from django.contrib import admin
from .models import Category,Home_page_pics,Social_ps,Roomz,place_details


# Register your models here.
admin.site.register(place_details)
admin.site.register(Category)
admin.site.register(Home_page_pics)
admin.site.register(Social_ps)
admin.site.register(Roomz)
