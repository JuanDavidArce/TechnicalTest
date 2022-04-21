"""Acces point Forms"""
# Django
import django.forms as forms


# Models
from companies.models import AccesPoint


class CreateAccesPointForm(forms.ModelForm):
    """Create form"""

    class Meta:
        model = AccesPoint
        fields = '__all__'

    
    def save(self):
        """Create Acces point."""
        data = self.cleaned_data
        AccesPoint.objects.create(**data)
