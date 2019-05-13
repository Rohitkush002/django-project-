from django import forms
from .models import Chat


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message']

    user_name = forms.CharField(max_length=40,
                                label="",
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control ',
                                        'placeholder': 'Email',
                                        'style': 'display:none',
                                        'value': 'Rohit'

                                    }))
