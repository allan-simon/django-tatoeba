from django import forms

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	remember = forms.BooleanField(required=False)
class RegisterForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()
	captcha = forms.CharField()
	termsOfUse = forms.BooleanField()

