from django.urls import path
from . import views

urlpatterns = [
    path("", views.student, name="student_list"),
    path("students/<int:student_id>/", views.student_detail, name="student_detail"),
    path("groups/", views.group, name="group_list"),
    path("groups/<int:group_id>/", views.group_detail, name="group_detail"),
    path("registry/", views.student_registry, name="student_registry"),
]