from django.shortcuts import redirect, render
from todo.forms import TodoAddForm
from todo.models import Todo

# Create your views here.
def home(request):
    return render(request, "todo/home.html")

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos
    }
    return render(request, "todo/todo_list.html", context)

def todo_create(request):
    form = TodoAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("todo-list")

    context = {
        "form": form
    }
    return render(request, "todo/todo_create.html", context)
