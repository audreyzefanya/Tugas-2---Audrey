from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from todolist.forms import taskform
from django.contrib import messages
from todolist.forms import taskform
from todolist.models import Task
from django.urls import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user = request.user)
    context = {
        'list_todolist' : data_todolist,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sign up success!')
            return redirect('todolist:login_user')
        
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        form = taskform(request.POST)
        form.instance.user = request.user
        form.instance.date = datetime.datetime.now()
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response
    else:
        form = taskform()
    return render(request, "createtask.html")

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

def show_json(request):
    data_todolist = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_todolist), content_type="application/json")

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(
            title = title, 
            description = description, 
            date = datetime.date.today(), 
            user = request.user)
        return JsonResponse(
            {
                "pk": task.pk,
                "fields": {
                    "title": task.title,
                    "description": task.description,
                    "date": task.date,
                },
            },
        )