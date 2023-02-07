from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    # todos = Todo.objects.all().filter(todo__contains='첫번째')
    todos = Todo.objects.all().order_by('-pk')
    return render(request,'todo_app/index.html', {'todos':todos,})