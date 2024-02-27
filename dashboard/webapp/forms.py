from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .models import Records

from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# register/create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

# login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Creating a record

class CreateFormRecord(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['first_name','last_name', 'email','phone','address','city','state','country']    

# updating a record

class UpdateFormRecord(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['first_name','last_name', 'email','phone','address','city','state','country']            