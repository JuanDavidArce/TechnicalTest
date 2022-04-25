"""Users Forms"""
# Django
import django.forms as forms


# Models
from users.models import User


# Utils
from utils.email import *


# Python
import threading


class CreateForm(forms.ModelForm):
    """Create form"""

    password_confirmation = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','address','phone','country','state','city','email','password']
        help_texts = {
            'username': None,
        }
        widgets = {
            "password": forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),

        }

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user"""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        thread = threading.Thread(target=send_user_mail, 
                                    args= (user,'Registration in access control platform','emails/email_notification_register.html', {'password':data['password']}, ))
        thread.start()