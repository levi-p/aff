from django import forms

class search_form(forms.Form):
    Search=forms.CharField(max_length=30)

