from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Todo

# Create your views here.


@login_required(login_url='accounts:login')
def home_view(request):
    todos = request.user.todos.all()
    return render(request, "todo/home.html", {'todos': todos})

@login_required(login_url="accounts:login")
def add_view(request):
    if request.method == "POST":
        title = request.POST['title']
        category = request.POST['category']
        importancy = request.POST['importancy']

        Todo.objects.create(
            user=request.user,
            title=title,
            category=category,  
            importancy=importancy)
        return redirect('todo:home')


    return render(request, "todo/add.html")



@login_required(login_url='accounts:login')
def edit_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "POST":
        todo.title = request.POST['title']
        todo.category = request.POST['category']
        todo.importancy = request.POST['importancy']
        todo.save()
        return redirect('todo:home')
    
    return render(request, 'todo/edit.html', {'todo': todo})

@login_required(login_url='accounts:login')
def delete_view(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=pk, user=request.user)
        todo.delete()
    
    return redirect('todo:home')

