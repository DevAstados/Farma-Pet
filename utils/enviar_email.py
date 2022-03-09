import smtplib
import ssl
from email.message import EmailMessage

from django.shortcuts import render
from django.template.loader import get_template, render_to_string

from silpan import settings


def sending(pedido, items, endereco):
    context = ssl.create_default_context()

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls(context=context)
        smtp.ehlo()
        print(getattr(settings, "EMAIL_HOST_USER"))
        print(getattr(settings, "EMAIL_HOST_PASSWORD"))
        smtp.login(getattr(settings, "EMAIL_HOST_USER"), getattr(settings, "EMAIL_HOST_PASSWORD"))
        smtp.send_message(modelaEmail(pedido, items, endereco))


def modelaEmail(pedido, items, endereco):
    msg = EmailMessage()
    msg['Subject'] = "Pedido realizado com sucesso!"
    msg['From'] = getattr(settings, "EMAIL_HOST_USER", None)
    msg['To'] = pedido.cliente.email
    msg.set_content('content')
    msg.add_alternative(render_to_string('modelo_email.html', {'pedido': pedido, 'items': items, 'endereco': endereco}), subtype='html')

    return msg
