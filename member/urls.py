from django.urls import path

from member import views

urlpatterns = [
    path('create-worker/', views.CustomWorkerCreateView.as_view(), name='create_worker'),
    path('create-member/', views.CustomMemberCreateView.as_view(), name='create_member'),
    path('worker-list/', views.WorkerListView.as_view(), name='worker_list'),
    path('member-list/', views.MemberListView.as_view(), name='member_list'),
    path('detail-worker/<int:pk>', views.WorkerDetailView.as_view(), name='detail_worker'),
    path('detail-account/', views.AccountDetailView.as_view(), name='detail_account'),
]