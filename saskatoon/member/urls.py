from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views, autocomplete

urlpatterns = [

    # CREATE VIEWS
    path('person/create/',
         views.PersonCreateView.as_view(),
         name='person-create'),

    path('beneficiary/create/',
         views.OrganizationCreateView.as_view(),
         name='beneficiary-create'),

    # UPDATE VIEWS
    path('person/update/<int:pk>/',
         views.PersonUpdateView.as_view(),
         name='person-update'),

    path('beneficiary/update/<int:pk>/',
         views.OrganizationUpdateView.as_view(),
         name='beneficiary-update'),


    # AUTO-COMPLETE VIEWS
    re_path(r'^actor-autocomplete/$',
            autocomplete.ActorAutocomplete.as_view(),
            name='actor-autocomplete'),

    re_path(r'^person-autocomplete/$',
            autocomplete.PersonAutocomplete.as_view(),
            name='person-autocomplete'),

    re_path(r'^pickleader-autocomplete/$',
            autocomplete.PickLeaderAutocomplete.as_view(),
            name='pickleader-autocomplete'),

    re_path(r'^owner-autocomplete/$',
            autocomplete.OwnerAutocomplete.as_view(),
            name='owner-autocomplete'),

    re_path(r'^contact-autocomplete/$',
            autocomplete.ContactAutocomplete.as_view(),
            name='contact-autocomplete'),

    # AUTH VIEWS
    path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name ='reset_password'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name ='password_reset_done'),

    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(),
         name ='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name ='password_reset_complete'),
]
