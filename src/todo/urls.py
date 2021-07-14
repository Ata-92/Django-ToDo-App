from django.urls import path
from .views import home, todo_create, todo_list, todo_update

urlpatterns = [
    path("", home, name="home_page"),
    path("list/", todo_list, name="todo-list"),
    path("create/", todo_create, name="create"),
    path("<int:id>/update/", todo_update, name="update"),
]
