from django.urls import path

from job import views

urlpatterns = [
    path('create_job/', views.JobCreateView.as_view(), name='create-job'),
    path('list_job/', views.JobListView.as_view(), name='list-jobs'),
    path('detail_job/<int:pk>', views.JobDetailView.as_view(), name='detail-job'),
]