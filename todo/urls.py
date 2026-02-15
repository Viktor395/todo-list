from django.urls import path
from .views import (
    TaskListView, 
    TaskCreateView, 
    TaskUpdateView, 
    TaskDeleteView,
    TagListView, 
    TagCreateView, 
    TagUpdateView, 
    TagDeleteView,
    TaskStatusUpdateView
)

app_name = "todo"

urlpatterns = [
    # Завдання (Tasks)
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle/", TaskStatusUpdateView.as_view(), name="task-toggle"),
    
    # Теги (Tags)
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
