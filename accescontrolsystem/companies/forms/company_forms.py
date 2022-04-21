"""Company forms"""
# Django
import django.forms as forms


# Models
from companies.models import Company


class CreateCompanyForm(forms.ModelForm):
    """Create form"""

    class Meta:
        model = Company
        exclude = '__all__'

    
    def save(self):
        """Create Company."""
        data = self.cleaned_data
        Company.objects.create(**data)
