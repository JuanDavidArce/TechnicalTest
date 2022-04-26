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
        widgets = {
            'start_time': forms.TimeInput(
                                        attrs={'type': 'time',
                                        'min':"00:00", 'max':"23:59", 'step':"1"},),
            'ending_time': forms.TimeInput(
                                        attrs={'type': 'time',
                                        'min':"00:00", 'max':"23:59", 'step':"1"},)

        }

    
    def save(self):
        """Create Schedule."""
        data = self.cleaned_data
        Schedule.objects.create(**data)


class UpdateScheduleForm(forms.ModelForm):
    """Create form"""

    class Meta:
        model = Schedule
        exclude = ['acces_point']
        widgets = {
            'start_time': forms.TimeInput(
                                        attrs={'type': 'time',
                                        'min':"00:00", 'max':"23:59", 'step':"1"},),
            'ending_time': forms.TimeInput(
                                        attrs={'type': 'time',
                                        'min':"00:00", 'max':"23:59", 'step':"1"},)

        }

    def save(self,**kwargs):
        """update Schedule."""
        data = self.cleaned_data
        if kwargs.get('pk',False):
            schedule = Schedule.objects.filter(pk = kwargs['pk'])
            schedule.update(**data)
        