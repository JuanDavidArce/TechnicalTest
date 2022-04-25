"""Invitations views"""

# Forms
from companies.forms import   CreateInvitationForm


# Django
from django.urls.base import reverse_lazy,reverse
from django.views.generic import FormView,UpdateView,DeleteView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Models
from users.models import User
from companies.models import Invitation, company
from companies.models import Company


class DeleteInvitationView(DeleteView,LoginRequiredMixin):
    """Delete Invitation"""
    model= Invitation
    def get_success_url(self) :
        return reverse_lazy('companies:invitations_list',kwargs={'pk':self.kwargs['pk']})


class CreateInvitationView(LoginRequiredMixin,FormView):
    """Schedule register view"""
    template_name='invitations/create.html'
    form_class=CreateInvitationForm

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)
    
    def get_form(self):
        company =  Company.objects.filter (pk=self.kwargs['pk']) 
        form = super().get_form(self.form_class)
        form.fields['company'].queryset = company
        return form

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context ['pk_company'] = self.kwargs['pk']
        return context

    def get_success_url(self) :
        return reverse_lazy('companies:invitations_list',kwargs={'pk':self.kwargs['pk']})
 
class ListInvitationsView(LoginRequiredMixin,ListView):
    """List of Companies"""
    template_name= 'invitations/list.html'
    Model= Invitation
    context_object_name='invitations'

    def get_queryset(self):
        return Invitation.objects.filter(company__pk = self.kwargs['pk'])
