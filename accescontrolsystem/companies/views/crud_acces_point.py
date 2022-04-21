"""Companies views"""

# Forms
import pdb

from companies.forms import  CreateAccesPointForm


# Django
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView,FormView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from companies.models.accespoint import AccesPoint


# Models
from companies.models import Company



class CreateAccesPointView(LoginRequiredMixin,FormView):
    """Company register view"""
    template_name='acces_points/create.html'
    form_class=CreateAccesPointForm
    success_url=reverse_lazy('users:indexadministrator')

    def form_valid(self, form):
        """Save form data"""
        form.save(company=Company.objects.get(administrator = self.request.user))
        return super().form_valid(form)

class DetailAccesPointView(LoginRequiredMixin,DetailView):
    """Detail acces point"""
    model = AccesPoint
    template_name='acces_points/detail.html'


class UpdateAccesPointView(LoginRequiredMixin,UpdateView):
    """Update acces point"""
    template_name='acces_points/update.html'
    model = AccesPoint
    fields = ['name', 'address','email', 'geolocation', 'is_active']
    
    def get_success_url(self):
        """Return to users detail"""
        pdb.set_trace()
        pk=self.get_object().pk
        return reverse('companies:detailaccespoint',kwargs={'pk':pk})
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['schedules'] = self.get_object().schedules_acces_point.all()
        return context
    
class DeleteAccesPointView(DeleteView,LoginRequiredMixin):
    """Delete Company"""
    model= AccesPoint
    success_url= reverse_lazy('users:indexadministrator')
   