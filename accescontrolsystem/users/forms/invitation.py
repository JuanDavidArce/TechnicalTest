"""Users Forms"""
# Django
import django.forms as forms


# Models
from users.models import User
from companies.models import Invitation,Company


# Utils
from utils.email import *


# Python
import threading


class CreateUserByInvitationForm(forms.ModelForm):
    """Create form"""

    password_confirmation = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}))
    class Meta:
        model = User
        fields = ['first_name','company','last_name','username','address','phone','country','state','city','email','password']
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
        """Verify password confirmation match. and invitation"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        email = data['email']
        company = data['company']

        invitation = Invitation.objects.filter(email = email,company = company)
        if not invitation:
            raise forms.ValidationError('You dont have an invitation.')
        invitation.delete()
        return data

    def save(self):
        """Create user"""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        thread = threading.Thread(target=send_user_mail, 
                                    args= (user,'Registration in access control platform',
                                    'emails/email_notification_register_company.html', 
                                    {'company':data['company'],'operation':'notification registration company'}, ))
        thread.start()