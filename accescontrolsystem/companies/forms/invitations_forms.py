"""Invitations Forms"""
# Django
import email
import django.forms as forms


# Models
from companies.models import Invitation
from users.models import User


# Utils
from utils.email import *


# Python
import threading


class CreateInvitationForm(forms.ModelForm):
    """Create form"""

    class Meta:
        model = Invitation
        fields = ['company','email']

    
    def save(self):
        """Create Invitation."""
        data = self.cleaned_data
        Invitation.objects.create(**data)
        thread = threading.Thread(target=send_user_mail, 
                                    args= (User(email=data['email'],
                                    first_name = 'None',
                                    last_name = 'None'),
                                    'Invitation',
                                    'emails/invitation.html', 
                                    {'operation':'invitation',
                                    'company':data['company']}))
        thread.start()

