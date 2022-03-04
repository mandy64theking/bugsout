from django import forms
from django.contrib.auth.models import User
class signUpForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password =forms.CharField()
	class Meta:
		model = User
		fields = {'username','email','password'}
class signInForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField()
	class Meta:
		model = User
		fields={'username','password'}