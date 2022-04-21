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
                            ListCompaniesView,
                            DeleteAccesPointView,
                            DetailAccesPointView,
                            UpdateAccesPointView,
                            UpdateScheduleView,
                            DetailScheduleView,
                            DeleteScheduleView)

app_name = 'companies'
urlpatterns = [

    # Companies
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

    path('listcompanies/',
    ListCompaniesView.as_view(),
        name='list'),

    path('manage',
    ManageCompaniesView.as_view(),
    name = 'manage'),


    # Acces points
    path('accespoint/create',
    CreateAccesPointView.as_view(),
    name = 'create_acces_point'),

    path('accespoint/<int:pk>/detail/',
    DetailAccesPointView.as_view(),
    name = 'detailaccespoint'),

    path('accespoint/<int:pk>/update/',
    UpdateAccesPointView.as_view(),
    name = 'updateaccespoint'),

    path('accespoint/<int:pk>/delete/',
    DeleteAccesPointView.as_view(),
    name = 'deleteaccespoint'),


    # Schedule
    path('accespoint/schedule/create',
    CreateScheduleView.as_view(),
    name = 'create_schedule'),


    path('accespoint/schedule/<int:pk>/detail/',
    DetailScheduleView.as_view(),
    name = 'detailschedule'),

    path('accespoint/schedule/<int:pk>/update/',
    UpdateScheduleView.as_view(),
    name = 'updateschedule'),

    path('accespoint/schedule/<int:pk>/delete/',
    DeleteScheduleView.as_view(),
    name = 'deleteschedule'),
]
