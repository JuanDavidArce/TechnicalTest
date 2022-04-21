"""Company forms"""
# Django
import django.forms as forms


# Models
from companies.models import Company
from users.models import User


class CreateCompanyForm(forms.ModelForm):
    """Create form"""

    class Meta:
        model = Company
        fields = '__all__'

    
    def save(self):
        """Create Company."""
        data = self.cleaned_data
        user = User.objects.get(pk = data['administrator'].pk)
        user.role = 'administrator'
        user.save()
        Company.objects.create(**data)
