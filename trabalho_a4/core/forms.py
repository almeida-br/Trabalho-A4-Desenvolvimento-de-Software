from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

class LoginForm(AuthenticationForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
      
class loginView(LoginView):
    template_name="login.html"
    authentication_form = LoginForm 
