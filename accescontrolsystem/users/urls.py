"""Users URLS"""

# Django
from django.urls import path


# Views 
from users.views import CreateView,LoginView

app_name = 'users'
urlpatterns = [
    path('create',
    CreateView.as_view(),
    name = 'create'),

    path('login',
    LoginView.as_view(),
    name = 'login')
]
