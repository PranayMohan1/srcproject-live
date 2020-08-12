from django.urls import path
from activity import views

urlpatterns = [
    path('activity/', views.MemberViewSet.as_view()),
    path('activity/<int:pk>/', views.MemberDetail.as_view()),
]