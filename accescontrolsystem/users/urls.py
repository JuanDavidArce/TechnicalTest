"""Users URLS"""

# Django
from django.urls import path


# Views 
from users.views import (CreateView, DeleteUserView,
                        LoginView,
                        LogoutView,
                        IndexUserRootView,
                        ManageUsersView,
                        DetailUserView,
                        ListUsersView,
                        UpdateUserView)

app_name = 'users'
urlpatterns = [
    path('create/',
    CreateView.as_view(),
    name = 'create'),

    path('<int:pk>/detail/',
    DetailUserView.as_view(),
    name = 'detail'),

    path('<int:pk>/update/',
    UpdateUserView.as_view(),
    name = 'update'),

    path('<int:pk>/delete/',
    DeleteUserView.as_view(),
    name = 'delete'),

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
    
    path('listusers/',
    ListUsersView.as_view(),
        name='list'),

    
]
