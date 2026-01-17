from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path(
        "tasks/<int:task_id>/comments/",
        views.comment_list,
        name="list"
    ),
    path(
        "tasks/<int:task_id>/comments/create/",
        views.comment_create,
        name="create"
    ),
    path(
        "comments/<int:pk>/edit/",
        views.comment_update,
        name="update"
    ),
    path(
        "comments/<int:pk>/delete/",
        views.comment_delete,
        name="delete"
    ),
]
