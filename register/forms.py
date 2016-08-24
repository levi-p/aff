from django import forms
from .models import Sign_up
#

class Sign_up_form(forms.ModelForm):
    
    class Meta():
        model=Sign_up
        fields=('Name','Email','enter_password','password')

        widgets={'enter_password':forms.PasswordInput(attrs={}),'password':forms.PasswordInput(attrs={}),'Email':forms.EmailInput()}
