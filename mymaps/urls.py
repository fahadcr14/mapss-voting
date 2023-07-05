from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('questions.html',views.questions, name='questions'),
    path('dashboard.html',views.dashboard_view, name='dashboard'),
    path('dashboardview',views.dashboardview, name='dashboardview'),

    path('submit_questionnaire/', views.submit_questionnaire, name='submit_questionnaire'),
    path('api/voters/',views.get_voter_data, name='voters_api'),
    path('api/names/',views.get_persons, name='names_api'),
    path('api/get-pct-by-ward/', views.get_pct_by_ward, name='get_pct_by_ward'),
    path('api/get-steet-by-pct/', views.get_street_by_pct, name='get_street_by_pct'),
    path('api/filterby',views.filterbywardpct, name='api/filterby'),
    path('api/get_pcts/',views.get_pcts, name='api/get_pcts/'),

    #path('inject', views.inject_voters_from_csv, name='inject'),



]
