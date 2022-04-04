import json

from django.contrib.auth import authenticate
from django.contrib import auth, messages
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View

from usuario.models import CustomUser


class CreateUserGoogle(View):
    def get(self):
        pass

    def post(self):
        pass


class login_cliente(View):
    def get(self, request, *args, **kwargs):
        template_name = 'login.html'

        return render(request, template_name, context=None)

    def post(self, request, *args, **kwargs):
        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)

        usuario = authenticate(request, username=requestJson['username'], password=requestJson['password'])

        if not usuario:
            messages.add_message(request, messages.ERROR, "Usuário ou senha incorreto")

            return redirect(request.path_info)
        elif usuario.tipo_usuario != 1:
            messages.add_message(request, messages.ERROR, "Usuário não é cliente")
            return redirect(request.path_info)

        auth.login(request, user=usuario)

        return redirect('home')
