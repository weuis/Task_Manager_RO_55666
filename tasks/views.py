from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from projects.models import Project


@login_required
def task_list(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    tasks = project.tasks.all()

    return render(
        request,
        "tasks/task_list.html",
        {"project": project, "tasks": tasks}
    )


@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect("tasks:list", project_id=project.id)
    else:
        form = TaskForm()

    return render(
        request,
        "tasks/task_create.html",
        {"form": form, "project": project}
    )


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:list", project_id=task.project.id)
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "tasks/task_update.html",
        {"form": form, "task": task}
    )


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)

    if request.method == "POST":
        project_id = task.project.id
        task.delete()
        return redirect("tasks:list", project_id=project_id)

    return render(
        request,
        "tasks/task_delete.html",
        {"task": task}
    )
