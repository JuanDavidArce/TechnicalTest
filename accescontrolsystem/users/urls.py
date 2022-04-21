"""Users URLS"""

# Django
from django.urls import path


# Views 
from users.views import (CreateView,
                        LoginView,
                        LogoutView,
                        IndexUserRootView,
                        ManageUsersView,
                        DetailUserView)

app_name = 'users'
urlpatterns = [
    path('create/',
    CreateView.as_view(),
    name = 'create'),

    path('detail/<int:pk>/',
    DetailUserView.as_view(),
    name = 'detail'),

    path('login/',
    LoginView.as_view(),
    name = 'login'),

    path('logout/',
    LogoutView.as_view(),
        name='logout'),
    
    path('indexroot/',
    IndexUserRootView.as_view(),
        name='indexroot'),
    
    path('manage/',
    ManageUsersView.as_view(),
        name='manage'),

    
]
