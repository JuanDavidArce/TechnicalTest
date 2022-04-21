"""Users views"""

# Forms
from users.forms import  RegisterForm


# Django
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView,FormView,UpdateView,DeleteView,ListView,TemplateView




# Create your views here.
class RegisterView(FormView):
    """Users register view"""
    template_name='users/register.html'
    form_class=RegisterForm
    success_url=reverse_lazy('users:register')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)