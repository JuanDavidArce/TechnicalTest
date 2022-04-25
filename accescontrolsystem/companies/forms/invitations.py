"""Invitations Forms"""
# Django
import django.forms as forms


# Models
from companies.models import Invitation


class CreateInvitationForm(forms.ModelForm):
    """Create form"""

    class Meta:
        model = Invitation
        fields = '__all__'

    
    def save(self):
        """Create Schedule."""
        data = self.cleaned_data
        Invitation.objects.create(**data)