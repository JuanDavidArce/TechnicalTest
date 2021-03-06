"""Users views"""

# Forms
import pdb
from users.forms import  CreateUserByInvitationForm,CreateForm


# Django
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView,FormView,UpdateView,DeleteView,ListView,TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin


# Models
from users.models import User
from companies.models import AccesPoint, Company

# Create your views here.
class CreateView(LoginRequiredMixin,FormView):
    """Users register view"""
    template_name='users/create.html'
    form_class=CreateForm
    success_url=reverse_lazy('users:manage')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)

        

class LoginView(auth_views.LoginView):
    """Login view"""
    template_name='users/login.html'

    def get_success_url(self) -> str:
        if self.request.user.role == 'root':
            return reverse('users:indexroot')
        elif self.request.user.role == 'administrator':
            return reverse('users:indexadministrator')
        else:
            return reverse('users:login')

        
    
class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Logout View"""


class IndexUserRootView(LoginRequiredMixin,TemplateView):
    """Index root"""
    template_name='users/index_root.html'

class IndexAdministratorView(LoginRequiredMixin,ListView):
    """Index administrator"""
    template_name='users/index_admin.html'
    Model= AccesPoint
    context_object_name='accespoints'
    paginate_by = 3
    def get_queryset(self):
        return AccesPoint.objects.filter(company__administrator = self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company' ]= Company.objects.get(administrator = self.request.user)
        return context


class ManageUsersView(LoginRequiredMixin,TemplateView):
    """Index root"""
    template_name='users/manage.html'


class DetailUserView(LoginRequiredMixin,DetailView):
    """Detail user view"""
    model = User
    template_name='users/detail.html'


class ListUsersView(LoginRequiredMixin,ListView):
    """List of users"""
    template_name= 'users/list.html'
    Model= User
    context_object_name='users'
    def get_queryset(self):
        return User.objects.all()

class UpdateUserView(LoginRequiredMixin,UpdateView):
    """Update profile view"""
    template_name='users/update.html'
    model=User
    fields=['first_name','last_name','email','username','phone','country','city','state','company','address']

    def get_success_url(self):
        """Return to users detail"""
        pk=self.object.pk
        return reverse('users:detail',kwargs={'pk':pk})

class DeleteUserView(DeleteView,LoginRequiredMixin):
    """Delete Post"""
    model=User
    success_url= reverse_lazy('users:list')

class CreateUserInvitationView(FormView):
    """Users register by invitation view"""
    template_name='users/create_by_invitation.html'
    form_class=CreateUserByInvitationForm
    success_url=reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)
    
    def get_form(self):
        form = super().get_form(self.form_class)
        form.fields['company'].queryset = Company.objects.filter(pk = self.kwargs['pk']) 
        return form
    


