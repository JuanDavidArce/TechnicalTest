"""Schedules Forms"""
# Django
import django.forms as forms


# Models
from companies.models import Schedule


class CreateScheduleForm(forms.ModelForm):
    """Create form"""

    class Meta:
        model = Schedule
        fields = '__all__'

    
    def save(self):
        """Create Schedule."""
        data = self.cleaned_data
        Schedule.objects.create(**data)