__author__ = 'Administrator'
from django import forms

class RegisterForm(forms.Form):
    Email = forms.EmailField()
    Username = forms.CharField(max_length=100)
    Password = forms.CharField()
    Password2 = forms.CharField()
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password', '')
        password2 = cleaned_data.get('password2', '')

        if password != password2:
            raise forms.ValidationError("passwords not match")

        return cleaned_data

class loginForm(forms.Form):
    Username = forms.CharField(max_length=100)
    Password = forms.CharField()

class createBlogForm(forms.Form):
    title = forms.CharField()
    Post_text = forms.CharField()
    pub_date = forms.CharField()

