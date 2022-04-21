"""Users URLS"""

# Django
from django.urls import path


# Views 
from users.views import CreateView

app_name = 'users'
urlpatterns = [
    path('create',
    CreateView.as_view(),
    name = 'create')
]
