from django import forms
# from .models import Author
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = '__all__'


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']