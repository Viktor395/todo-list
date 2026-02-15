from django.shortcuts import get_object_or_404, redirect
from django.views import generic, View
from .models import Task, Tag

class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"

class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"

class TaskStatusUpdateView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo:index")
