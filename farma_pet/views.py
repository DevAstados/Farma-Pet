from django.contrib import auth
from django.shortcuts import render, redirect


def administracao(request):
    if request.method == 'GET':
        template_name = 'base_administracao.html'

        return render(request=request, template_name=template_name)


def login(request):
   pass


def Logout(request):
    if request.method == 'GET':
        auth.logout(request)

        return redirect('..')
