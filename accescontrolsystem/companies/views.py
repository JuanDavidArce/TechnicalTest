"""Companies views"""

# Forms
import pdb
from companies.forms import  CreateCompanyForm,CreateAccesPointForm, CreateScheduleForm


# Django
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView,FormView,UpdateView,DeleteView,ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Models
from users.models import User
from companies.models import Company


class CreateCompanyView(LoginRequiredMixin,FormView):
    """Company register view"""
    template_name='companies/create.html'
    form_class=CreateCompanyForm
    success_url=reverse_lazy('companies:create')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)
    
    def get_form(self):
        form = super().get_form(self.form_class)
        form.fields['administrator'].queryset = User.objects.filter(role = 'user' )
        return form



class CreateAccesPointView(LoginRequiredMixin,FormView):
    """Company register view"""
    template_name='acces_points/create.html'
    form_class=CreateAccesPointForm
    success_url=reverse_lazy('companies:create_acces_point')

    def form_valid(self, form):
        """Save form data"""
        form.save(company=Company.objects.get(administrator = self.request.user))
        return super().form_valid(form)


class CreateScheduleView(LoginRequiredMixin,FormView):
    """Schedule register view"""
    template_name='schedule/create.html'
    form_class=CreateScheduleForm
    success_url=reverse_lazy('companies:create_schedule')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)

class ManageCompaniesView(TemplateView):
    """Manage companies view"""
    template_name='companies/manage.html'


