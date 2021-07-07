from django.urls import path
from . import views

urlpatterns = [
    path('',views.TeacherListView.as_view(), name="teachers"),
    path('teacher/<int:pk>',views.TeacherDetailView.as_view(), name="teacher"),
]