from django.contrib import admin
from .models import Category,Home_page_pics,Social_ps,Roomz,Place_details


# Register your models here.
admin.site.register(Place_details)
admin.site.register(Category)
admin.site.register(Home_page_pics)
admin.site.register(Social_ps)
admin.site.register(Roomz)
