from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path
from sitebase import views

urlpatterns = [

    url(r'^$',
        views.Index.as_view(),
        name='home'),

    url(r'^jsoncal',
        views.JsonCalendar.as_view(),
        name='calendarJSON'),

    re_path(r'^calendar/$',
            views.Calendar.as_view(),
            name='calendar'),

    path('equipment_points/',
         views.EquipmentPointsPDFView.as_view(),
         name='equipment-points'),

    path('privacy_policy/',
         views.PrivacyPolicyView.as_view(),
         name='privacy_policy'),

    path('volunteer_waiver/',
         views.VolunteerWaiverPDFView.as_view(),
         name='volunteer-waiver'),
]
