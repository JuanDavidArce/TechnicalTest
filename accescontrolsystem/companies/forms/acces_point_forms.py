"""Acces point Forms"""
# Django
import django.forms as forms


# Models
from companies.models import AccesPoint


class CreateAccesPointForm(forms.ModelForm):
    """Create form"""

    class Meta:
        model = AccesPoint
        exclude = ['company']

    
    def save(self):
        # CHECK TO ASSING COMPANY
        """Create Acces point."""
        data = self.cleaned_data
        AccesPoint.objects.create(**data)
