"""Users views"""

# Forms
from pyexpat import model
from users.forms import  CreateForm


# Django
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView,FormView,UpdateView,DeleteView,ListView,TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin


# Models
from users.models import User

# Create your views here.
class CreateView(LoginRequiredMixin,FormView):
    """Users register view"""
    template_name='users/create.html'
    form_class=CreateForm
    success_url=reverse_lazy('users:create')

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
            return reverse('companies:create_acces_point')
        

    
class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Logout View"""


class IndexUserRootView(LoginRequiredMixin,TemplateView):
    """Index root"""
    template_name='users/index_root.html'


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
    fields=['first_name','last_name','email','username','phone','country','city','state','company']

    def get_success_url(self):
        """Return to users detail"""
        pk=self.object.pk
        return reverse('users:detail',kwargs={'pk':pk})

class DeleteUserView(DeleteView,LoginRequiredMixin):
    """Delete Post"""
    model=User
    success_url= reverse_lazy('users:list')