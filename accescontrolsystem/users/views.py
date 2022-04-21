"""Users views"""

# Forms
from users.forms import  CreateForm


# Django
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView,FormView,UpdateView,DeleteView,ListView,TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin






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

class IndexUserRootView(TemplateView):
    """Index root"""
    template_name='users/index_root.html'


