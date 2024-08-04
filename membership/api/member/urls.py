from django.urls import path
from membership.api.member import views  

urlpatterns = [
    path('', views.MemberListCreateView.as_view(), name='member_list_create'),
    path('<int:pk>/', views.MemberDetailView.as_view(), name='member_detail'),
]
