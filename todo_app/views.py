from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin #로그인 조건을 만족해야 다음으로 통과
from .models import Todo

# Create your views here.
def index(request):
    # todos = Todo.objects.all().filter(todo__contains='첫번째')
    todos = Todo.objects.all().order_by('-pk')
    return render(request,'todo_app/index.html', {'todos':todos,})


def Todos(request):
    # todos = Todo.objects.all().filter(todo__contains='첫번째')
    todos = Todo.objects.all().order_by('-pk')
    return render(request,'todo_app/todos.html', {'todos':todos,})


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo #CreateView에서 '모델명_form'이라는 이름의 html을 알아서 찾음 -> templates/todo_app 안에서 알아서 찾음(이래서 폴더 안에 넣은거임)
    fields = ['todo','description','important']
    
    