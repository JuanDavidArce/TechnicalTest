"""Companies views"""

# Forms
from companies.forms import  CreateCompanyForm,UpdateCompanyForm


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
    success_url=reverse_lazy('companies:list')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)
    def get_form(self):
        form = super().get_form(self.form_class)
        form.fields['administrator'].queryset = User.objects.filter(role = 'user' )
        return form
    

class ManageCompaniesView(LoginRequiredMixin,TemplateView):
    """Manage companies view"""
    template_name='companies/manage.html'


class DetailCompanyView(LoginRequiredMixin,DetailView):
    """Detail company view"""
    model = Company
    template_name='companies/detail.html'


class ListCompaniesView(LoginRequiredMixin,ListView):
    """List of Companies"""
    template_name= 'companies/list.html'
    Model= Company
    context_object_name='companies'

    def get_queryset(self):
        return Company.objects.all()
    

class UpdateCompanyView(LoginRequiredMixin,UpdateView):
    """Update Company"""
    template_name='companies/update.html'
    model = Company
    form_class = UpdateCompanyForm
    
    def get_success_url(self):
        """Return to users detail"""
        pk=self.get_object().pk
        return reverse('companies:detail',kwargs={'pk':pk})
    
    def get_form(self):
        form = super().get_form(self.form_class)
        form.fields['administrator'].queryset = User.objects.filter(role = 'user') 
        if self.get_object().administrator:
            form.fields['administrator'].queryset = User.objects.filter(role = 'user') | User.objects.filter(pk=self.get_object().administrator.pk)
        return form
    
    def form_valid(self, form):
        """Save form data"""
        form.save(pk=self.get_object().pk,administrator = self.get_object().administrator)
        return super().form_valid(form)


class DeleteCompanyView(DeleteView,LoginRequiredMixin):
    """Delete Company"""
    model=Company
    success_url= reverse_lazy('companies:list')


