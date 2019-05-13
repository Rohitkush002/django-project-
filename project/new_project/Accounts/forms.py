from django import forms
from . models import NewUsers
class UserForm(forms.ModelForm):
    class Meta:
        model = NewUsers
        fields = ['username','password','email','mobile']

    username = forms.CharField(max_length=40,
                               label="Username",
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Username'
                                   }))
    password = forms.CharField(max_length=40,
                               label="password",
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'password'
                                   }))
    email = forms.CharField(max_length=40,
                               label="Email",
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Email'
                                   }))
    mobile = forms.CharField(max_length=40,
                            label="Mobile",
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Mobile'
                                }))







class LoginForm(forms.Form):

    username = forms.CharField(max_length=40,
                             label="Username",
                             widget=forms.TextInput(
                                 attrs = {
                                     'class' : 'form-control',
                                     'placeholder':'Username'
                                }))

    password = forms.CharField(max_length=40,
                            label="Password",
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter Password'
                                }))

class ChangePassword(forms.ModelForm):

    class Meta:
        model = NewUsers
        fields = ['password']

    password = forms.CharField(max_length=40,
                            label="Old Password",
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Old Password'
                                }))
    newPassword = forms.CharField(max_length=40,
                                     label="New Password",
                                     widget=forms.TextInput(
                                         attrs={
                                             'class': 'form-control',
                                             'placeholder': 'New Password'
                                         }))
    repeatPassword = forms.CharField(max_length=40,
                                  label="Repeat Password",
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Repeat Password'
                                      }))