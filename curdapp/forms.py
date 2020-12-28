from django import forms
from curdapp.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','phone','password']