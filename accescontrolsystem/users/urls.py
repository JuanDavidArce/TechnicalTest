"""Users URLS"""

# Django
from django.urls import path


# Views 
from users.views import CreateView,LoginView,LogoutView,IndexUserRootView

app_name = 'users'
urlpatterns = [
    path('create',
    CreateView.as_view(),
    name = 'create'),

    path('login',
    LoginView.as_view(),
    name = 'login'),

    path('logout/',
    LogoutView.as_view(),
        name='logout'),
    
    path('indexroot/',
    IndexUserRootView.as_view(),
        name='indexroot'),

    
]
