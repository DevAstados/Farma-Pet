import json

from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from cliente.models import Cliente
from usuario.models import CustomUser


class CreateUserGoogle(View):
    def get(self):
        pass

    def post(self):
        pass


class verificacao(View):
    def get(self, request, *args, **kwargs):
        usuario = request.user
        try:

            cliente = Cliente.objects.get(usuario_id=usuario.pk)

        except Cliente.DoesNotExist:
            usuario.tipo_usuario = 'C'
            usuario.save()
            print('nao tem cliente')
            return HttpResponseRedirect(reverse_lazy('usuario:cadastro_cliente'))


class login_cliente(View):
    def get(self, request, *args, **kwargs):
        template_name = 'login.html'

        return render(request, template_name, context=None)

    def post(self, request, *args, **kwargs):
        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)

        usuario = CustomUser(username=requestJson['username'], tipo_usuario='C')
        usuario.set_password(requestJson['password'])
        usuario = authenticate(username=requestJson['username'], password=requestJson['password'])

        if not usuario:
            messages.add_message(request, messages.ERROR, "Usuário ou senha incorreto")

            return redirect(request.path_info)
        elif usuario.tipo_usuario != 'C':
            messages.add_message(request, messages.ERROR, "Usuário não é cliente")
            return redirect(request.path_info)

        auth.login(request, user=usuario)

        return redirect('home')


class cadastro_cliente(View):
    def get(self, request, *args, **kwargs):
        template_name = 'cadastro.html'

        return render(request, template_name, context=None)

    def post(self, request, *args, **kwargs):
        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)

        if not request.user:
            usuario = CustomUser.popular(requestJson, tipo_usuario='C')
        else:
            usuario = request.user
            requestJson['email'] = usuario.email
        cliente = Cliente.popular_cliente(requestJson, usuario)
        usuario.first_name = cliente.nome
        usuario.last_name = cliente.sobrenome
        usuario.save()
        cliente.save()
