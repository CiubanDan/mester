from django.urls import path

from member import views

urlpatterns = [
    path('create-user/', views.CustomMemberCreateView.as_view(), name='create_user'),
]