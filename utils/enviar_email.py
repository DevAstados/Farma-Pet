import base64
import os
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .Google import Create_Service

from django.shortcuts import render
from django.template.loader import get_template, render_to_string

from farma_pet import settings


CLIENT_SECRET_FILE = 'auth/client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
NAME_SITE = 'Farma Pet'

def sending(email):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    emailMsg = 'Cadastro realizado com sucesso na '  + NAME_SITE
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = email
    mimeMessage['subject'] = 'Cadastro realizado'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)





'''
def sendng(pedido, items, endereco):
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
'''