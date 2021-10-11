# from django.conf  import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                         document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect
from crime.views import login
urlpatterns = [
    path('', views.index, name="index"),
    path('login_view/', views.login_view, name="login_view"),
    path('registerPage/', views.registerPage, name="registerPage"),
    path('logout',views.logoutUser, name='logout'),
    path('error401', views.error401, name='error401'),
    path('home_Hq/', views.homeHq, name="home_Hq"),
    path('home_Station/', views.homeStation, name="home_Station"),
    path('home_Officer/', views.homeOfficer, name="home_Officer"),
    path('createRIBStation/', views.createRIBStation, name="createRIBStation"),
    path('createOfficer/', views.createOfficer, name="createOfficer"),
    path('officerList/', views.officerList, name="officerList"),
    path('RIBstationList/', views.RIBstationList, name="RIBstationList"),
    path('suspect/<str:pk_susp>/', views.suspect, name="suspect"),
    path('witnes/<str:pk_susp>/', views.witnes, name="witnes"),
    path('caseList/', views.caseList, name="caseList"),
    path('evidence/', views.evidenceList, name="evidence"),
    path('create_case/', views.createCase, name="create_case"),
    path('update_case/<str:pk>/', views.updateCase, name="update_case"),
    path('delete_case/<str:pk>/', views.deleteCase, name="delete_case"),
    path('create_suspect/<str:case_pk>/', views.createSuspect, name="create_suspect"),
    path('suspectList/', views.suspectList, name="suspectList"),
    path('update_suspect/<str:case_pk>/', views.updateSuspect, name="update_suspect"),
    path('delete_suspect/<str:case_pk>/', views.deleteSuspect, name="delete_suspect"),
    path('create_evidence/<str:suspect_pk>/', views.createEvidence, name="create_evidence"),
    path('update_evidence/<str:pk>/', views.updateEvidence, name="update_evidence"),
    path('createReporter/<str:suspect_pk>/', views.createReporter, name="create_reporter"),
    path('reporterList/', views.reporterList, name="reporterList"),
    path('createMurderForm/', views.createMurderForm, name="createMurderForm"),
    path('createViolentForm/', views.createViolentForm, name="createViolentForm"),
    path('createRobberyForm/', views.createRobberyForm, name="createRobberyForm"),
    path('viewCaseSuspects/<str:case_pk>/', views.viewCaseSuspects, name="viewCaseSuspects"),

 ]