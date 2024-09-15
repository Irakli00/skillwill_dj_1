from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=25)
    password = forms.CharField(label='password', max_length=25, widget=forms.PasswordInput)