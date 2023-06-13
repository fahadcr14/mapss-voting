from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('questions.html',views.questions, name='questions'),
    path('submit_questionnaire/', views.submit_questionnaire, name='submit_questionnaire'),
    path('api/voters/',views.get_voter_data, name='voters_api'),
    path('api/names/',views.get_persons, name='names_api'),


]
