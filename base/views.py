from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, User, Mark
from .form import TaskForm, MyUserCreationForm, MarkForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('login').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "No such user was found")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Login or password is incorrect")

    context = {'page': page, } #{% url 'logout' %}
    return render(request, 'base/login.html', context)

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)   
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Check login and password correctness")        
    context = {'form': form}
    return render(request, 'base/login.html', context)

def home(request):
    tasks = Task.objects.all()
    task_number = tasks.count()
    return render(request, 'base/home.html', 
                  {'tasks': tasks, 'task_number': task_number})

def task(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}
    return render(request, 'base/task.html', context)

@login_required(login_url = 'login')
def createTask(request):
    form = TaskForm()
    #form_mark = MarkForm()

    if request.method == 'POST':
        Task.objects.create(
            host=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            duedate = request.POST.get('duedate')
        )
        return redirect('home')

    context = {'form': form, }
    return render(request, 'base/task_form.html', context)

@login_required(login_url = 'login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    # if request.user != task.host: # add something here
    #     return HttpResponse("This task is for creators or compleaters")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'task': task}
    return render(request, 'base/task_form.html', context)

@login_required(login_url = 'login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.user != task.host: # add something here
        return HttpResponse("This task can be deleted by owner creator")

    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'task':task}
    return render(request, 'base/delete_task.html', context)



