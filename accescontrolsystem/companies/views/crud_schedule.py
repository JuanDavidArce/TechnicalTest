"""Schedule views"""

# Forms
from companies.forms import   CreateScheduleForm,UpdateScheduleForm


# Django
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView,FormView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
import django.forms as forms


# Models
from companies.models import Schedule
from companies.models import AccesPoint
from users.models import User



class DetailScheduleView(LoginRequiredMixin,DetailView):
    """Detail schedule"""
    model = Schedule
    template_name='schedules/detail.html'

class DeleteScheduleView(DeleteView,LoginRequiredMixin):
    """Delete shcedule"""
    model= Schedule
    success_url= reverse_lazy('users:indexadministrator')



class UpdateScheduleView(LoginRequiredMixin,UpdateView):
    """Update schedule"""
    template_name='schedules/update.html'
    form_class = UpdateScheduleForm
    model = Schedule

    def get_success_url(self):
        """Return to users detail"""
        pk=self.get_object().pk
        return reverse('users:indexadministrator')
    
    def form_valid(self, form):
        """Save form data"""
        form.save(pk=self.get_object().pk)
        return super().form_valid(form)
    
    def get_form(self):
        acces_point =  self.get_object().acces_point
        form = super().get_form(self.form_class)
        form.fields['user'].queryset = User.objects.filter(company = acces_point.company ).exclude(role ='administrator')
        return form
    


class CreateScheduleView(LoginRequiredMixin,FormView):
    """Schedule register view"""
    template_name='schedules/create.html'
    form_class=CreateScheduleForm
    success_url=reverse_lazy('users:indexadministrator')


    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)
    
    def get_form(self):
        acces_point =  AccesPoint.objects.filter (pk=self.kwargs['pk']) 
        form = super().get_form(self.form_class)
        form.fields['user'].queryset = User.objects.filter(company = acces_point[0].company ).exclude(role ='administrator')
        form.fields['acces_point'].queryset = acces_point
        return form
 
    