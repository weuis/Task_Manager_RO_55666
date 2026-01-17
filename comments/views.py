from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from tasks.models import Task
from .models import Comment
from .forms import CommentForm


@login_required
def comment_list(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        project__owner=request.user
    )
    comments = task.comments.select_related("user")

    return render(
        request,
        "comments/comment_list.html",
        {"task": task, "comments": comments}
    )

@login_required
def comment_create(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        project__owner=request.user
    )

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            return redirect("comments:list", task_id=task.id)
    else:
        form = CommentForm()

    return render(
        request,
        "comments/comment_create.html",
        {"form": form, "task": task}
    )


@login_required
def comment_update(request, pk):
    comment = get_object_or_404(
        Comment,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(
                "comments:list",
                task_id=comment.task.id
            )
    else:
        form = CommentForm(instance=comment)

    return render(
        request,
        "comments/comment_update.html",
        {"form": form, "comment": comment}
    )


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(
        Comment,
        pk=pk,
        user=request.user
    )
    task_id = comment.task.id

    if request.method == "POST":
        comment.delete()
        return redirect(
            "comments:list",
            task_id=task_id
        )

    return render(
        request,
        "comments/comment_delete.html",
        {"comment": comment}
    )
