from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from rbac import models
from .forms import LoginForm
import re
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
    request.session.clear()
    return redirect(reverse('login'))

def index(request):
    return render(request,'rbac/index.html')


def m1(request):
    return render(request,'rbac/m1.html')


def m2(request):
    return render(request,'rbac/m2.html')


def m3(request):
    return render(request,'rbac/m3.html')


def m4(request):
    return render(request,'rbac/m4.html')

