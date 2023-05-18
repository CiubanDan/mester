from django.urls import path

from job import views

urlpatterns = [
    path('create_job/', views.JobCreateView.as_view(), name='create-job')
]