from django.shortcuts import render, redirect
import datetime
from django.urls import reverse
from django.shortcuts import render
from todolist.forms import TaskForm
from todolist.models import MyTask
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.models import MyTask

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_list = MyTask.objects.filter(user=request.user)
    context = {
        'task_list': task_list,
        'nama': request.user.username,
        'last_login' : request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Task telah berhasil dibuat!')
            return redirect('todolist:show_todolist')
    context = {'form':form}
    return render(request, 'create-task.html', context)

 
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def update(request, id):
    task_list = MyTask.objects.filter(id=id)
    task = task_list[0]
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete(request, id):
    task_list = MyTask.objects.filter(id=id)
    task = task_list[0]
    task.delete()
    return redirect('todolist:show_todolist')