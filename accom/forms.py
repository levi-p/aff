from django import forms
from details.models import Home_page_pics

class search_form(forms.Form):
    Search=forms.CharField()
    

class iso(forms.ModelForm):
    class Meta:


        model = Home_page_pics
        fields=('Hpic','Dis')

