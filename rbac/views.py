from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.conf import settings

from rbac import models
from .forms import LoginForm

# Create your views here.
# RBAC（Role-Based Access Control，基于角色的访问控制）

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            try:
                user=models.User.objects.get(username=form.cleaned_data['username'])
            except:
                message='用户名错误'
                context={'message':message}
                return request(request,'rbac/login.html',context)

            if user.password == form.cleaned_data['password']:
                from .init_permission import init_permission
                init_permission(request,user)
                return redirect(reverse('index'))
            else:
                message='密码错误！'
                context={'message':message}
                return render(request,'rbac/login.html',context)
        else:
            context={'form':form}
            return render(request,'rbac/login.html',context)

    else:
        form=LoginForm()
        context={'form':form}
        return render(request,'rbac/login.html',context)


def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

def index(request):
    path_action=request.session.get(settings.SESSION_PERMISSION_ACTION_KEY)
    path=request.path
    action=path_action[path]
    context={'action':action}
    return render(request,'rbac/index.html',context)


def m1(request):
    path_action=request.session.get(settings.SESSION_PERMISSION_ACTION_KEY)
    path=request.path
    action=path_action[path]
    context={'action':action}
    return render(request,'rbac/m1.html',context)


def m2(request):
    path_action=request.session.get(settings.SESSION_PERMISSION_ACTION_KEY)
    path=request.path
    action=path_action[path]
    context={'action':action}
    return render(request,'rbac/m2.html',context)


def m3(request):
    path_action=request.session.get(settings.SESSION_PERMISSION_ACTION_KEY)
    path=request.path
    action=path_action[path]
    context={'action':action}
    return render(request,'rbac/m3.html',context)


def m4(request):
    path_action=request.session.get(settings.SESSION_PERMISSION_ACTION_KEY)
    path=request.path
    action=path_action[path]
    context={'action':action}
    return render(request,'rbac/m4.html',context)

