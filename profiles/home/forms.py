from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import models
from django import forms
from .models import Profile

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = models.User
		fields = ["username", "email", "password1", "password2"]
	
class ProfileCreationForm(forms.Form):
	name = forms.CharField(max_length=30)
