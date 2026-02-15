from django.shortcuts import get_object_or_404, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Task, Tag
from .forms import TaskForm, TagForm

class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo:index')
    template_name = 'todo/task_form.html'

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo:index')
    template_name = 'todo/task_form.html'

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('todo:index')
    template_name = 'todo/task_confirm_delete.html'

class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"

class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('todo:tag-list')
    template_name = 'todo/tag_form.html'

class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('todo:tag-list')
    template_name = 'todo/tag_form.html'

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('todo:tag-list')
    template_name = 'todo/tag_confirm_delete.html'

class TaskStatusUpdateView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo:index")
