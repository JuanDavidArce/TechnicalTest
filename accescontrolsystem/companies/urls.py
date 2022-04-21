"""Companies URLS"""

# Django
from django.urls import path


# Views 
from companies.views import (CreateCompanyView, 
                            CreateAccesPointView, 
                            CreateScheduleView,
                            ManageCompaniesView)

app_name = 'companies'
urlpatterns = [
    path('create',
    CreateCompanyView.as_view(),
    name = 'create'),

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
