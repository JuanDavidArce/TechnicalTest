"""Companies views"""

# Forms
from companies.forms import  CreateCompanyForm,CreateAccesPointForm, CreateScheduleForm


# Django
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView,FormView,UpdateView,DeleteView,ListView,TemplateView



class CreateCompanyView(FormView):
    """Company register view"""
    template_name='companies/create.html'
    form_class=CreateCompanyForm
    success_url=reverse_lazy('companies:create')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)


class CreateAccesPointView(FormView):
    """Company register view"""
    template_name='acces_points/create.html'
    form_class=CreateAccesPointForm
    success_url=reverse_lazy('companies:create_acces_point')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)


class CreateScheduleView(FormView):
    """Schedule register view"""
    template_name='schedule/create.html'
    form_class=CreateScheduleForm
    success_url=reverse_lazy('companies:create_schedule')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)