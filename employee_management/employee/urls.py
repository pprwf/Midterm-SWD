from django.urls import path, include
from . import views

urlpatterns = [
    path("employee/", views.EmployeeView.as_view(), name = "employee"),
    path("position/", views.PositionView.as_view(), name = "position"),
    path("project/", views.ProjectView.as_view(), name = "project"),
    path("project/<int:project_id>/edit/", views.ProjectEditView.as_view(), name = "edit"),
    path("project/<int:project_id>/edit/<int:employee_id>/", views.ProjectEditView.as_view(), name = "edit"),
    path("layout/", views.layout)
]
