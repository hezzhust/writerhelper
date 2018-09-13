from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)
    password_check = forms.CharField(max_length=50)
    email = forms.CharField(max_length=150)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30)

