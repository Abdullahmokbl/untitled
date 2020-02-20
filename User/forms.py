from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

