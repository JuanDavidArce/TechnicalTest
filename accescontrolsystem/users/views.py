"""Users views"""

# Forms
from users.forms import  CreateForm


# Django
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView,FormView,UpdateView,DeleteView,ListView,TemplateView
from django.contrib.auth import views as auth_views





# Create your views here.
class CreateView(FormView):
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

