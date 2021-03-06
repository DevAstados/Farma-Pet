import json

from django.contrib.sites import requests
from django.core.exceptions import ValidationError
from social_django.models import UserSocialAuth
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
import requests
from farma_pet import settings
from usuario.my_captcha import FormWithCaptcha
from utils import enviar_email
from cliente.models import Cliente, Endereco
from usuario.models import CustomUser


class verificacao(View):
    def get(self, request, *args, **kwargs):
        usuario = request.user
        print(request.user.first_name)

        try:
            cliente = Cliente.objects.get(usuario_id=usuario.pk)
        except Cliente.DoesNotExist:
            usuario.tipo_usuario = 'C'
            usuario.save()
            return HttpResponseRedirect(reverse_lazy('usuario:cadastro_cliente'))
        try:
            endereco = Endereco.objects.get(cliente=cliente)
        except Endereco.DoesNotExist:
            return HttpResponseRedirect(reverse_lazy('usuario:cadastro_endereco'))
        return redirect(reverse_lazy('home'))


class login_cliente(View):

    def get(self, request, *args, **kwargs):
        template_name = 'login.html'
        context = {"captcha": FormWithCaptcha,
                   }
        return render(request, template_name, context=context)


    def post(self, request, *args, **kwargs):
        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)


        if requestJson['g-recaptcha-response'] == '':
            messages.error(request, 'Verifique o reCAPTCHA.')
            return redirect(request.path_info)

        try:
            s = FormWithCaptcha(request.POST)
            s.fields['captcha'].validate(requestJson['g-recaptcha-response'])
        except ValidationError as error:
            messages.error(request, 'ReCAPTCHA inv??lido, por favor tente novamente!!.')
            return redirect(request.path_info)

        usuario = CustomUser(email=requestJson['username'], tipo_usuario='C')
        usuario.set_password(requestJson['password'])
        usuario = authenticate(email=usuario.email, password=requestJson['password'])

        if not usuario:
            messages.add_message(request, messages.ERROR, "Usu??rio ou senha incorreto")

            return redirect(request.path_info)
        elif usuario.tipo_usuario != 'C':
            messages.add_message(request, messages.ERROR, "Usu??rio n??o ?? cliente")
            return redirect(request.path_info)
        auth.login(request, user=usuario)

        return redirect(reverse_lazy('home'))


class cadastro_cliente(View):
    def get(self, request, *args, **kwargs):
        template_name = 'cadastro_cliente.html'
        context = {}
        context['usuario'] = request.user
        return render(request, template_name, context=context)

    def post(self, request, *args, **kwargs):
        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)

        if not request.user.is_authenticated:
            usuario = CustomUser.popular(requestJson, tipo_usuario='C')
        else:
            usuario = request.user
            requestJson['email'] = usuario.email
        cliente = Cliente.popular_cliente(requestJson, usuario)
        usuario.first_name = cliente.nome
        usuario.last_name = cliente.sobrenome

        #enviar_email.sending(cliente.email)

        usuario.save()
        cliente.save()
        usuario.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user=usuario)

        return redirect(reverse_lazy('usuario:cadastro_endereco'))


class cadastro_endereco(View):
    def get(self, request, *args, **kwargs):
        template_name = 'cadastro_endereco.html'
        context = {}

        return render(request, template_name, context=context)

    def post(self, request, *args, **kwargs):
        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)
        cliente = Cliente.objects.get(usuario_id=request.user.pk)
        endereco = Endereco.populaEndereco(requestJson, cliente)
        endereco.save()

        return redirect(reverse_lazy('home'))


def Logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('home')
