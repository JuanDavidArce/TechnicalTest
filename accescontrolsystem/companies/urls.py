"""Companies URLS"""

# Django
from django.urls import path


# Views 
from companies.views import (CreateCompanyView, 
                            CreateAccesPointView, 
                            CreateScheduleView,
                            ManageCompaniesView,
                            DetailCompanyView,
                            UpdateCompanyView,
                            DeleteCompanyView,
                            ListCompaniesView)

app_name = 'companies'
urlpatterns = [
    path('create',
    CreateCompanyView.as_view(),
    name = 'create'),
    path('<int:pk>/detail/',
    DetailCompanyView.as_view(),
    name = 'detail'),

    path('<int:pk>/update/',
    UpdateCompanyView.as_view(),
    name = 'update'),

    path('<int:pk>/delete/',
    DeleteCompanyView.as_view(),
    name = 'delete'),

    path('listcomapanies/',
    ListCompaniesView.as_view(),
        name='list'),

    path('accespoint/create',
    CreateAccesPointView.as_view(),
    name = 'create_acces_point'),

    path('accespoint/schedule/create',
    CreateScheduleView.as_view(),
    name = 'create_schedule'),

    path('manage',
    ManageCompaniesView.as_view(),
    name = 'manage'),
]
