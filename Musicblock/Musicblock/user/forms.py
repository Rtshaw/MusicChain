from django import forms

from .models import UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = []
        fields=('username','password','email','first_name','ssn','file','gender')