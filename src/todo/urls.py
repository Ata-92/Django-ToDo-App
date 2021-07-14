from django.urls import path
from .views import home, todo_create, todo_list

urlpatterns = [
    path("", home, name="home_page"),
    path("list/", todo_list, name="todo-list"),
    path("create/", todo_create, name="create"),
]
