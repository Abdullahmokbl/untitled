# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import CreateUserForm
#from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.success(request, '{} is registered'.format(new_user))
            return redirect('movie:movies')
    else:
        form = CreateUserForm()
    return render(request, 'user/register.html', {'form':form})

def logina(request):
    if request.method == 'POST':
        #form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        #if form.is_valid():
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('movie:home')
        else:
            messages.success(request,"sdasasf")
            return redirect('movie:movies')
    #else:
    #   form = LoginForm()
    return render(request, 'user/login.html')

def logouta(request):
    logout(request)
    return render(request, 'user/logout.html')


def sign(request):
    return render(request, 'user/sign.html')


