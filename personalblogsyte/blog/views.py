from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template import RequestContext
from .models import Registration
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Blog


@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def posts(request):
    posts = Blog.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def login(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            return redirect("login")
    form = UserCreationForm()
    return render(request, 'login.html', {'form': form})


def acc_detail(request, id):
    try:
        acc = Registration.objects.get(id=-id)
    except Registration.DoesNotExist:
        raise Http404('Acc not found')
    return render(render, 'acc_detail.html', {'acc': acc})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request)
            return redirect("index")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request, 'signup.html', {'form': form})


@login_required
def post(request):
    posts = Blog.objects.all()
    return render(request, 'posts.html', {'posts': posts})
