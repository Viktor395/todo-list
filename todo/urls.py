from django.urls import path
from .views import (
    TaskListView, 
    TagListView, 
    TaskStatusUpdateView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/<int:pk>/toggle/", TaskStatusUpdateView.as_view(), name="task-toggle"),
]

app_name = "todo"
