from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
	email = forms.EmailField()
	captcha = forms.CharField()
	termsOfUse = forms.BooleanField()

