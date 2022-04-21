"""Users URLS"""

# Django
from django.urls import path


# Views 
from users.views import RegisterView

app_name = 'users'
urlpatterns = [
    path('register',
    RegisterView.as_view(),
    name = 'register')
]
