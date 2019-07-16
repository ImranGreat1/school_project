from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Did Not Match!")
        return confirm_password


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'defaultLoginFormEmail', 'class':'form-control mb-4', 'placeholder': 'E-Mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'defaultLoginFormPassword', 'class':'form-control mb-4', 'placeholder': 'Password'}))
